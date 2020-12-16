# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LolgamesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    
class Game(scrapy.Item):
    duration = scrapy.Field()
    timestamp = scrapy.Field()
    server = scrapy.Field()
    mmr = scrapy.Field()
    result = scrapy.Field()
    team_1 = scrapy.Field()
    team_2 = scrapy.Field()