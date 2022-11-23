# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class NewscrawlingItem(scrapy.Item):
    # define the fields for your item here like:
    press = scrapy.Field() # 신문사
    date = scrapy.Field() # 날짜
    article = scrapy.Field() # 본문


class NewscrawlingUrl(scrapy.Item):
    # define the fields for your item here like:
    url=scrapy.Field() # 기사 링크
    
