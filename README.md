## Craigslist scraper using Scrapy ('CrawlSpider')

This is an entry level crawler for helping beginners in understanding how Scrapy works in general. This particular crawler will retrieve all available listings from `"computer gigs"` section in all regions of the world and store in a CSV file using command line parameters.

How to use the script:<br>
`scrapy crawl cjscrap -o Cjoutput.csv -t CSV`

Script would fetch following fields:
- [x] Category URL
- [x] Post Title
- [x] Post URL
- [x] Date & Time

Future changes:
- [ ] Rolling Proxies support
- [ ] New field: Post description
- [ ] New field: Email / Phone of poster

> Approach me directly, If you want to participate in any manner.
