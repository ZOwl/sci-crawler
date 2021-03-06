# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ScicrawlerItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass

class SciItem(Item):
    title = Field()
    link = Field()

class PaperItem(Item):
    journal = Field()
    by = Field()
    title = Field()
