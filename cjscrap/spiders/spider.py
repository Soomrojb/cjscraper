import scrapy
from bs4 import BeautifulSoup
from scrapy import Request, Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor

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
		#Html = Selector(response)
		#Title = Html.xpath("//nav/div/h2")
		#CompGig = Html.xpath("//div/ul/li/a[contains(@href,'/search/cpg')]")
		#print response.url + "search/cpg"
		#yield {
		#	'test' : CompGig.extract(),
		#	'title' : Title.extract()[0],
		#	'url' : response.url,
		#	'parse_list' : (response.url + "/search/cpg"),
		#}
		#print response
		#Html = BeautifulSoup(response.body, 'html.parser')
		#NextURl = Html.find('a').get('href')
		#print NextURl
		#yield Request(response.urljoin(CompGig.extract()), callback=self.parse)
		yield Request((response.url + "search/cpg"), callback=self.parse_posts)

	def parse_posts(self, response):
		#print "new url = " + response.url
		Html = Selector(response)
		RowTitle = Html.xpath("//ul[contains(@class,'row')]/li//p")
		for Post in RowTitle:
			yield {
				'posturl' : response.urljoin(Post.xpath("a/@href").extract()[0]),
				'time' : Post.xpath("time/@datetime").extract(),
				'posttitle' : Post.xpath("a/text()").extract(),
				'parse_posts' : response.url,
			}

