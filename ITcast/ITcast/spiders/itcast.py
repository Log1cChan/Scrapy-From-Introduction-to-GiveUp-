# coding=utf-8

import scrapy
from ITcast.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    # Crawler Name essential
    name = 'itcast'
    allowed_domains = ['http://www.itcast.cn']  # Optional param
    # NO MORE THAN 16 URLS
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml'] # essential param

    def parse(self, response):
        # print (response.body)
        node_list = response.xpath("//div[@class='main_mask']")

        # Store all the item
        # items = []

        for node in node_list:
            # Create item for storing data
            item = ItcastItem()
            # .extract() change xpath object to Unicode String
            name = node.xpath("./h2/text()").extract()
            title = node.xpath("./h2/span/text()").extract()
            info = node.xpath("./p/text()").extract()

            item['name'] = (name[0])
            item['title'] = (title[0])
            item['info'] = (info[0])
            # items.append(item)

            # Return every item data, and Transfer data to pipelines
            # Meanwhile go back an execute the code followed
            yield item

        # return to engine, dont through pipelines
        # return items
        
        # return scrapy.Request(url)

        # pass
