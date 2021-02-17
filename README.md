# only use Docker for SPIDER
Spider를 통해 추출한 데이터를 Elasticsearch 에 저장
Elasticsearch는 repo: elktW 것 사용
Dockerfile_SPIDER 만 사용

utils.py 파일에서 아래 부분 수정해서 사용

connections.create_connection(hosts=[f'{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}']) <br>
EX)   connections.create_connection(hosts=[ 'http://elastic:changeme@localhost:9200/' ])


# lawlaw2
lawlaw2


# Install Spider Requirements

    $ pip3 install -r requirements.txt

# Spider Installation
          # setting elasticsearch IP in settings.py
    $ docker build -t law_go_kr_spider:v1.0 -f Dockerfile_SPIDER .
    $ docker run -it -d --restart unless-stopped  --network=host -h 127.0.0.1 --name law-spider law_go_kr_spider:v1.0 

# Portainer Installation

    $ docker run -d -p 9000:9000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer

    # Port = 9000 | Username = admin | Password = vK7eeGgE

# Elasticsearch-Kibana Installation

    $ docker build -t es_supported_nori:v1.0 -f Dockerfile_ES .
    $ docker run -d --restart unless-stopped  -p 9200:9200 -p 5601:5601 --name el_et_search es_supported_nori:v1.0

    # Port = 5601

# Elasticsearch Creating Index

    PUT law_go_kr
    {
        "mappings" : {
          "properties" : {
            "case_id" : {
              "type" : "keyword"
            },
            "detail_data_html" : {
              "type" : "text",
              "index": false
            },
            "detail_data_searchable" : {
              "type" : "keyword",
              "ignore_above" : 10922
            },
            "index_data" : {
              "type" : "keyword"
            }
          }
        }
    }

    
    Note : 
    Error : whose UTF8 encoding is longer than the max length 32766
    Solition: 32766 / 3 = 10922
    URL : https://www.elastic.co/guide/en/elasticsearch/reference/2.4/ignore-above.html

# Elasticsearch Creating Index From Console

    curl -v -XPUT "localhost:9200/law_go_kr" -H 'Content-Type: application/json' -d '
        {
            "mappings" : {
              "properties" : {
                "case_id" : {
                  "type" : "keyword"
                },
                "detail_data_html" : {
                  "type" : "text",
                  "index": false
                },
                "detail_data_searchable" : {
                  "type" : "keyword",
                  "ignore_above" : 10922
                },
                "index_data" : {
                  "type" : "keyword"
                }
              }
            }
        }
        
     '


# Elasticsearch Queries
   * Delete index
    
    DELETE law_go_kr

   * Search documents in index

    GET law_go_kr/_search


  * Search keyword in detail_data_searchable
  
    
    GET law_go_kr/_search
    {
      "query": {
        "wildcard": {
          "detail_data_searchable": {
            "value": "*Keyword*"
          }
        }
      }
    }

  * Search keyword in index_data
  
    
    GET law_go_kr/_search
    {
      "query": {
        "wildcard": {
          "index_data": {
            "value": "*Keyword*"
          }
        }
      }
    }





# Settings

The Crawler settings allows you to customize the behaviour of all Spider components, including the timeout, extensions, connections and spiders themselves.


### ELASTICSEARCH_HOST

Default: ``localhost``

The host that elasticsearch will use to establish the connection.


### ELASTICSEARCH_PORT

Default: ``9200``

The port that elasticsearch will use to establish the connection.


### DOWNLOAD_DELAY

Default: ``1s``

The amount of time (in secs) that the downloader should wait before downloading consecutive pages from the same website. This can be used to throttle the crawling speed to avoid hitting servers too hard. Decimal numbers are supported.

### REQUEST_POOL_SIZE

Default: ``1``

The maximum number of concurrent (i.e. simultaneous) word that will be performed by the Crawler downloader.


# Usage
         
    python3 main.py


