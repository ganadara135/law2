import logging
from elasticsearch_dsl import Search
from elasticsearch_dsl.connections import connections

from lawgokr.settings import ELASTICSEARCH_HOST, ELASTICSEARCH_PORT
from lawgokr.exceptions import ElasticSearchError

class Counter:
    def __init__(self, total_cases, saved_cases):
        self.total_cases = total_cases
        self.saved_cases = saved_cases


def logger(message):
    logging.warning(message)
    with open('../output.log', 'a') as file:
        file.write(message + '\n')


def create_connection():
    try:
        connections.create_connection(hosts=[f'{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}'])
    except Exception as e:
        logger(str(e))
        raise ElasticSearchError('Elasticsearch Connection Error')


def is_unique(model):
    response = Search(index="law_go_kr") \
        .query("match", case_id=model.case_id).execute()
    return False if response else True


def db_cases_count():
    s = Search(index='law_go_kr')
    s.from_dict({"query": {"wildcard": {"case_id": "*"}}})
    return s.count()
