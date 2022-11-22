# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MinutesItem(scrapy.Item):
    # define the fields for your item here like:
    file_url = scrapy.Field()
    date = scrapy.Field()