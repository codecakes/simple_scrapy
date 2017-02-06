# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import unicodedata
from scrapy import Item, Field
from scrapy.loader.processors import Join, Compose,  MapCompose, TakeFirst, Identity
from w3lib.html import remove_tags

# convert unicode from html to string
fn = lambda t: unicodedata.normalize('NFKD', t).encode('ascii', 'ignore')

class TutorialItem(Item):
    '''
    using ItemLoader
    '''
    # define the fields for your item here like:
    quote = Field(
        input_processor=MapCompose(remove_tags, fn),
        output_processor= TakeFirst()
    )
    author = Field(
        input_processor=MapCompose(remove_tags, fn),
        output_processor=TakeFirst()
    )
    tags = Field(
        input_processor=MapCompose(remove_tags, fn),
        output_processor=Identity()
    )
