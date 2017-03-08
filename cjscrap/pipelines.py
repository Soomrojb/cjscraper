# -*- coding: utf-8 -*-

# Database Structure
#	craigslistdb:
#		cjposts:
#			- serial (auto)
#			- posturl (text)
#			- time (text)
#			- posttitle (text)
#			- parse_posts (text)
#

import MySQLdb

class CraigsListPipeline(object):
	conn = None
	cursr = None

	def __init__(self):
		self.setupDBCon()

	def __del__(self):
		self.conn.close()

	def setupDBCon(self):
		# Database connectivity
		self.conn = MySQLdb.connect(host='localhost', user='admin', passwd='admin', db='craigslistdb')
		self.cursr = self.conn.cursor()

	def open_spider(self, spider):
		print
		print "----------------------------------------------"
		print "	Starting Craigslist Scrapper"
		print "----------------------------------------------"
		print

	def close_spider(self, spider):
		print
		print "----------------------------------------------"
		print "	Ending Craigslist Scrapper"
		print "----------------------------------------------"
		print

	def process_item(self, item, spider):
		posturl = item['posturl']
		time = item['time']
		posttitle = item['posttitle']
		parse_posts = item['parse_posts']
		
		# Queries
		query = "INSERT INTO cjposts (posturl, time, posttitle, parse_posts) VALUES ('%s', '%s', '%s', '%s')" % (posturl, time, posttitle, parse_posts)
		srcquery = "SELECT * FROM cjposts WHERE `posturl` = '%s' AND `posttitle` = '%s'" % (posturl, posttitle)
		self.cursr.execute(srcquery)
		if self.cursr.fetchone() is None:
			# Add only new records
			self.cursr.execute(query)
			self.conn.commit()
		return item
	
