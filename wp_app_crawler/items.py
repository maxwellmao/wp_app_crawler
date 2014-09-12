# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class WpAppItem(Item):
    # define the fields for your item here like:
    name = Field()
    price=Field()
    review_num=Field()
    fb_like=Field()
    tweet_num=Field()
    publisher=Field()
    size=Field()
    release_date=Field()
    works_with=Field()
    app_require=Field()
    lang=Field()
    description=Field()
    rating=Field()
    version=Field()
    url=Field()
    download_link=Field()
#    social_network=Field()
