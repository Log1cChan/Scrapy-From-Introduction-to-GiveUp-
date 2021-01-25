# Intro Scrapy
## Content   

- - -
## $Documentation$
https://docs.scrapy.org/en/latest/
- - -
## 1. Terminal Command
### (1) Starting a new Scrapy
1. cd into the destination folder
2. type **scrapy** and the output is below\
Usage:
  scrapy <command> [options] [args]\
\
Available commands:\
  **bench**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run quick benchmark test\
  commands      \
  **fetch**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fetch a URL using the Scrapy downloader\
  **genspider**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate new spider using pre-defined templates\
  **runspider**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run a self-contained spider (without creating a project)\
  **settings**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Get settings values\
  **shell**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Interactive scraping console\
  **startproject**&nbsp;&nbsp;Create new project\
  **version**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print Scrapy version\
  **view**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Open URL in browser, as seen by Scrapy\
\
  [ more ]      More commands available when run from project directory\
\
Use "scrapy <command> -h" to see more info about a command
3. Start a Scrapy\
`scrapy startproject ProjectName`
4. Start a Spider\
`scrapy genspider SpiderName`\
Usually execute this command in the folder named **'spiders'**\
e.g.\
`(base) Log1cs-MacBook-Pro:spiders logic$ scrapy genspider itcast "http://www.itcast.cn"`
5. Execute\
`scrapy crawl SpiderName`
- - - 
## 2. Introduction of Structure
1. **scrapy.cfg**: The configuration file of the proj
2. **mySpider/**: Python modules of proj, code will be export
3. **mySpider/items.py**: File Destination also stores the data you desire
4. **mySpider/pipelines.py**: Pipe file of proj
5. **mySpider/settings.py**: Setting file of proj
6. **mySprider/spiders/**: Store your crawler Code\

**yiled func**:\
if use:
`yield item` in the end of `items.py`, means you transfer the data to pipelines and next time enter the `items.py`, will execute the lines after it. Different from return: if return, the func will be finished but yield not.\
- - -
## 3. ITcast Crawler
### (1) Data in Need:
**info**: //div[@class='main_mask']/p  \
**rank**: //div[@class='main_mask']/h2/span \
**name**: //div[@class='main_mask']/h2
### (2) Modify `items.py`
```
class ItcastItem(scrapy.Item):
    # define the fields for your item here like:
    # Teacher Name
    name = scrapy.Field()
    # Teacher Rank
    title = scrapy.Field()
    # Teacher Info
    info = scrapy.Field()
    # pass
```
### (3) Modify `itcast.py` inside spiders folder
The **parse func** is essential to crawl the data desired\
```
    def parse(self, response):
        # print (response.body)
        node_list = response.xpath("//div[@class='main_mask']")

        # Store all the item
        items = []

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
            items.append(item)
        # return to engine
        return items
```
Can use the command below to generate json file to store the data we get:
`scrapy crawl itcast -o itcast.json`



