import elasticsearch_dsl as es


class LawSuitModel(es.Document):
    class Index:
        name = 'law_go_kr'

    case_id = es.Keyword()
    index_data = es.Keyword()
    detail_data_html = es.Text()
    detail_data_searchable = es.Keyword()
  