#!/usr/bin/env python
#  -*- coding: utf-8 -*-

from mongo_connect import article
import datetime

time = datetime.datetime.strptime('2017-01-31', '%Y-%m-%d')
all_statistics = []

for i in range(28):
    time = time + datetime.timedelta(1)
    time_str = datetime.datetime.strftime(time, '%Y-%m-%d')
    articles = article.find({'date': time_str})
    for article_item in articles:

        date = article_item['date']
        lang = article_item['lang']

        for key, value in article_item.iteritems():
            one_statistic = []
            one_statistic.append(date)
            one_statistic.append(lang)
            if key == '_id':
                continue
            if key == 'date':
                continue
            if key == 'lang':
                continue
            one_statistic.append(key)
            one_statistic.append(value)
            all_statistics.extend(one_statistic)

for i in range(0, len(all_statistics), 4):
    with open('article.txt', 'a') as f:
        line = str(all_statistics[i])+' '+str(all_statistics[i+1])+' '+str(all_statistics[i+2])+' '+str(all_statistics[i+3])
        f.write(line)
        f.write('\n')

