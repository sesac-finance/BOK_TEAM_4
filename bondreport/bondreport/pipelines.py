# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter, CsvItemExporter

# class BondreportPipeline:
#     def process_item(self, item, spider):
#         return item

class BondreportPipeline(object):
    def __init__(self):
        self.file = open("BondreportFile.csv", 'wb')
        self.exporter = CsvItemExporter(self.file, encoding = 'euc-kr')
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

