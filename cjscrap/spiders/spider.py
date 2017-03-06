import scrapy
from bs4 import BeautifulSoup
from scrapy import Request, Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from cjscrap.item import CjscrapItem

class CJScrapper(CrawlSpider):
	name = "cjscrap"
	allowed_domains = ["craigslist.org"]
	start_urls = ["http://www.craigslist.org/about/sites"]
	rules = (
		Rule(LxmlLinkExtractor(
            restrict_xpaths=(".//div/ul/li/a[contains(@href,'craigslist.org')]")),
			follow=False,
			callback='parse_list'
		),
		Rule(LxmlLinkExtractor(
			restrict_xpaths=(".//div/ul/li/a[contains(@href,'/search/cpg')]")),
			follow=False,
			callback='parse_posts'
		),
	)
	
	def parse_list(self, response):
		yield Request((response.url + "search/cpg"), callback=self.parse_posts)

	def parse_posts(self, response):
		items = CjscrapItem()
		Html = Selector(response)
		RowTitle = Html.xpath("//ul[contains(@class,'row')]/li//p")
		for Post in RowTitle:
			items['posturl'] = response.urljoin(Post.xpath("a/@href").extract()[0])
			items['time'] = Post.xpath("time/@datetime").extract()
			items['posttitle'] = Post.xpath("a/text()").extract()
			items['parse_posts'] = response.url
			yield items

