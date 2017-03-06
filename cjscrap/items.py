# -*- coding: utf-8 -*-

import scrapy

class CjscrapItem(scrapy.Item):
	posturl = scrapy.Field()
	time = scrapy.Field()
	posttitle = scrapy.Field()
	parse_posts = scrapy.Field()

