import pymongo


def connect_collection(uri, db, collection):
    client = pymongo.MongoClient(uri)
    con_db = client['%s' % db]
    con_collection = con_db['%s' % collection]
    return con_collection
hi_hades_uri = 'mongodb://172.31.16.89:27017/'
hi_hades_db = 'hi_hades'

metrics_uri = 'mongodb://172.31.21.61:27017/'
metrics_db = 'metrics'
content = connect_collection(metrics_uri, metrics_db, 'content')
article_count = connect_collection(metrics_uri, metrics_db, 'article_count')

# -echo add
article_uri = 'mongodb://127.0.0.1:27017/'
article_db = 'media_article'
article = connect_collection(article_uri, article_db, 'article_count')
# -echo add end


daily_statistics = connect_collection(hi_hades_uri, hi_hades_db, 'daily_statistics')
payment = connect_collection(hi_hades_uri, hi_hades_db, 'payment')
statistics = connect_collection(hi_hades_uri, hi_hades_db, 'statistics')
bloggers = connect_collection(hi_hades_uri, hi_hades_db, 'bloggers')
language_server = {"hi": {"uri": "mongodb://172.31.20.123:27017/"}, "en": {"uri": "mongodb://172.31.16.248:27017/"}}
user = connect_collection(hi_hades_uri, hi_hades_db, 'user')
user_profile = connect_collection(hi_hades_uri, hi_hades_db, 'user_profile')

