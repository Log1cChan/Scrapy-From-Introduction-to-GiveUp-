# Intro to Scrapy
## Content   
- [Intro to Scrapy](#intro-to-scrapy)
  - [Content](#content)
  - [$Documentation$](#documentation)
  - [1. Terminal Command](#1-terminal-command)
    - [(1) Starting a new Scrapy](#1-starting-a-new-scrapy)
  - [2. Introduction of Structure](#2-introduction-of-structure)
  - [3. ITcast Crawler--Intro](#3-itcast-crawler--intro)
    - [(1) Data in Need:](#1-data-in-need)
    - [(2) Modify `items.py`](#2-modify-itemspy)
    - [(3) Modify `itcast.py` inside spiders folder](#3-modify-itcastpy-inside-spiders-folder)
  - [4. ITcast Crawler--pipelines](#4-itcast-crawler--pipelines)
    - [Usage](#usage)
  - [5. Scrapy Shell](#5-scrapy-shell)
    - [(1) Start a Scrapy Shell CommandLine](#1-start-a-scrapy-shell-commandline)
    - [(2) Command in Scrapy Shell](#2-command-in-scrapy-shell)
    - [(3) Usage](#3-usage)
      - [**Selectors**](#selectors)
      - [**Xpath Expression**](#xpath-expression)
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
\
**yiled func**:\
if use:
`yield item` in the end of `items.py`, means you transfer the data to pipelines and next time enter the `items.py`, will execute the lines after it. Different from return: if return, the func will be finished but yield not.\
- - -
## 3. ITcast Crawler--Intro
### (1) Data in Need:
**info**: //div[@class='main_mask']/p  \
**rank**: //div[@class='main_mask']/h2/span \
**name**: //div[@class='main_mask']/h2
### (2) Modify `items.py`
``` python
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
``` python
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
\
Can use the command below to generate **json csv jsonl xml** file to store the data we get:\
`scrapy crawl itcast -o itcast.json`\
`scrapy crawl itcast -o itcast.csv`\
`scrapy crawl itcast -o itcast.xml`\
\
**Website** parse json:\
http://www.json.cn\
- - - 
## 4. ITcast Crawler--pipelines
### Usage
In `itcast.py`, change the `return` to `yield` in the loop:\
`yield item`\
\
Then modify **`pipelines.py`**\
```python
from itemadapter import ItemAdapter
import json

class ItcastPipeline:
    # Optional
    def  __init__(self):
        self.f = open("itcast_pipeline.json", "w")

    # Get items from itcast.py item [Essential func]
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False)
        self.f.write(content)
        return item

    # Optional
    def close_spider(self, spider):
        self.f.close
```
\
Then Enable `**settings.py**`\
```python
# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'ITcast.pipelines.ItcastPipeline': 300, # The number here means priority small-->high prio
}
```
\
`Stressed`: Execute the command in the folder where you wanna put your data in. Like the data folder in this proj\
- - -
## 5. Scrapy Shell
### (1) Start a Scrapy Shell CommandLine
`scrapy shell "url-link"`\
e.g.\
`scrapy shell "http://www.itcast.cn/channel/teacher.shtml"`
### (2) Command in Scrapy Shell
```
[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x7f8fd73bd820>
[s]   item       {}
[s]   request    <GET http://www.itcast.cn/channel/teacher.shtml>
[s]   response   <200 http://www.itcast.cn/channel/teacher.shtml>
[s]   settings   <scrapy.settings.Settings object at 0x7f8fd73bd790>
[s]   spider     <DefaultSpider 'default' at 0x7f8fd77fddf0>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects 
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser
```
### (3) Usage
With **Scrapy Shell**, you can crawl the website easily. But the hinge of this Shell is to check if your **programmar** is right or not. After testing, you can use the available statement in your scrapy proj.\
\
Here is an Example:
```python
In [0]: item_list = response.xpath("//h3").extract()
In [1]: for item in item_list:
    ...:     print(item)
```
#### **Selectors**
**xpath()**: input the xpath expression, and return a selector list contains all the nodes which are corresponding to the expression\
**extract()**: Serialize the node to Unicode String and return the list\
**css()**: Similar to BeatifulSoup4, input css expression and return list\
**re()**: Input RegEx and **return list(Unicode)**
#### **Xpath Expression**
```
/html/head/title: Select <title> in <head> in <HTML>
/html/head/title/text(): Select the text inside the tag above
//td: Select all <tag> element
//div[@class="xxx"]: Select all div which has attribute: class="xxx"
```


