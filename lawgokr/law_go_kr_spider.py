import requests
from bs4 import BeautifulSoup
from time import sleep
from concurrent.futures import ThreadPoolExecutor

import lawgokr.requirements_lawsuits as rl
import lawgokr.requirements_cases as rc
from lawgokr.models import LawSuitModel
from lawgokr.logger import message
from lawgokr.utils import create_connection, is_unique, Counter, db_cases_count

from lawgokr.settings import REQUEST_POOL_SIZE, DOWNLOAD_DELAY
from math import ceil, floor


class LawgokrSpider(object):
    _lawsuits_selector = 'ul.left_list_bx li'
    _lawsuits_total_count_selector = '#readNumDiv strong'
    create_connection()

    @staticmethod
    def get_lawsuits(pages, pages_size, saved_pages):
        message('Getting case ids')

        for current_page in range(saved_pages + 1, pages + 1):
            while True:
                response = requests.post(url=rl.url,
                                         headers=rl.headers,
                                         params=rl.params,
                                         cookies=rl.cookies,
                                         data=rl.data(current_page, pages_size),
                                         timeout=None)

                if 'error500' not in response.text:
                    break

            yield response

    @classmethod
    def parse_lawsuits(cls, response):
        message('Parsing cases')
        soup = BeautifulSoup(response.content, 'lxml')

        lawsuits = soup.select(cls._lawsuits_selector)

        items = []
        for lawsuit in lawsuits:
            item = LawSuitModel()
            item.case_id = lawsuit.get('id').replace('licPrec', '')
            item.index_data = lawsuit.get_text()
            items.append(item)

        return items

    @staticmethod
    def get_case(model):
        sleep(DOWNLOAD_DELAY)
        message(f'Getting case details id = {model.case_id}')
        response = requests.post(url=rc.url,
                                 headers=rc.headers,
                                 cookies=rc.cookies,
                                 data=rc.data(model.case_id))
        html = response.text
        text = BeautifulSoup(response.content, 'html.parser').get_text().strip()

        return text, html

    @classmethod
    def get_outmax(cls):
        response = requests.post(url=rl.url,
                                 headers=rl.headers,
                                 params=rl.params,
                                 cookies=rl.cookies,
                                 data=rl.data(1, 1))
        sleep(5)
        return int(cls.get_total_cases(response))

    @classmethod
    def get_total_cases(cls, response):
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.select_one(cls._lawsuits_total_count_selector).get_text().replace(',', '')

    @classmethod
    def run(cls):
        total_cases = cls.get_outmax()
        saved_cases = db_cases_count()

        message(f'Total case count = {total_cases}')
        pages_size = 200
        pages = ceil(total_cases / pages_size)
        saved_pages = floor(saved_cases / pages_size)

        counter = Counter(total_cases, saved_cases)

        for lawsuits_content in cls.get_lawsuits(pages, pages_size, saved_pages):

            lawsuits = cls.parse_lawsuits(lawsuits_content)

            if not lawsuits:
                message('Did not find new cases..')

            with ThreadPoolExecutor(max_workers=REQUEST_POOL_SIZE) as executor:
                for lawsuit in lawsuits:
                    executor.submit(
                        cls.get_and_save_case,
                        lawsuit=lawsuit,
                        counter=counter
                    )

        message('Done')

    @classmethod
    def get_and_save_case(cls, lawsuit, counter):
        if is_unique(lawsuit):
            counter.saved_cases += 1
            message(f'{counter.total_cases}/{counter.saved_cases}')

            text, html = cls.get_case(lawsuit)
            lawsuit.detail_data_html = html
            lawsuit.detail_data_searchable = text
            lawsuit.save()

            message(f'Saving case id = {lawsuit.case_id}')


if __name__ == '__main__':
    spider = LawgokrSpider()
    spider.run()
