# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewscrawlingItem(scrapy.Item):
    # define the fields for your item here like:
    news_name = scrapy.Field() #신문사 이름
    date = scrapy.Field() #기사 날짜
    url = scrapy.Field() # 기사링크
    pass