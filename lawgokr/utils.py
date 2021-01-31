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


# es = Elasticsearch(
#     [
#         'http://user:secret@localhost:9200/',
#         'https://user:secret@other_host:443/production'
#     ],
#     verify_certs=True
# )


def create_connection():
    try:
        # connections.create_connection(hosts=[f'{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}'])
        connections.create_connection(hosts=[ 'http://elastic:changeme@localhost:9200/' ])
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
