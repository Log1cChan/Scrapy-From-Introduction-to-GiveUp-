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
`scrapy genspider SpiderName`
Usually execute this command in the folder named **'spiders'**\
e.g.\
`(base) Log1cs-MacBook-Pro:spiders logic$ scrapy genspider itcast "http://www.itcast.cn"`
5. Execute\
`scrapy crawl SpiderName`

