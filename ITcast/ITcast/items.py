# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastItem(scrapy.Item):
    # define the fields for your item here like:
    # Teacher Name
    name = scrapy.Field()
    # Teacher Rank
    title = scrapy.Field()
    # Teacher Info
    info = scrapy.Field()
    # pass
