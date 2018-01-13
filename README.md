## Craigslist scraper using Scrapy ('CrawlSpider')

This is an entry level crawler for helping beginners in understanding how Scrapy works in general. This particular crawler will retrieve all available listings from `"computer gigs"` section in all regions of the world and store in ~~a CSV file using command line parameters~~ MySQL database.

How to use the script:<br>
`scrapy crawl cjscrap`<br>
`scrapy crawl cjscrap -o Cjoutput.csv -t CSV`

Script would fetch following fields:
- [x] Category URL
- [x] Post Title
- [x] Post URL
- [x] Date & Time

New Features:
- [x] Rotating User agents
- [x] Rotating Proxies support
- [x] MySQLdb support

Future changes:
- [ ] New field: Post description
- [ ] New field: Email / Phone of poster

Required Repos:
- [x] `pip install scrapy`
- [x] `pip install mysqldb`
- [x] `pip install beautifulsoup4`
- [x] `pip install scrapy-random-useragent`
- [x] `pip install scrapy-rotating-proxies`
- [x] `apt-get install python-mysqldb`

Additional Repos for Windows:
- [x] `pip install wheel`
- [x] `easy_install mysql-python`
- [x] `Install VCForPython27.msi`

> Approach me directly, If you want to participate in any manner.
