# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter, CsvItemExporter
from scrapy.utils.project import get_project_settings
SETTINGS = get_project_settings()
from scrapy.exceptions import DropItem
# from scrapy import log

class NewscrawlingPipeline:
    def process_item(self, item, spider):
        return item

#CSV 파일로 저장하는 클래스
# class CsvPipeline(object):
#     def __init__(self):
#         self.file = open("newsCrawl.csv", 'wb')
#         self.exporter = CsvItemExporter(self.file, encoding='utf-8')
#         self.exporter.start_exporting()
 
#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.file.close()
 
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
