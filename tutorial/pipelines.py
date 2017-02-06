# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

class DuplicatesPipeline(object):
    def __init__(self):
        self.seen = {}
    
    def process_item(self, item, spider):
        if item["author"] not in self.seen:
            self.seen[item["author"]] = item
            quote = item["quote"]
            tags = item["tags"]
            self.seen[item["author"]] = {
                "author": item["author"],
                "quote": [item["quote"]],
                "tags": item["tags"]
                }
        else:
            self.seen[item["author"]]["quote"] += [item["quote"]]
            self.seen[item["author"]]["tags"] += item["tags"]
            item.update(self.seen[item["author"]])
        return item
            
        
    

