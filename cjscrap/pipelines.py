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
    def process_item(self, item, spider):
		conn = None
		curr = None
		query = "INSERT INTO cjposts (posturl, time, posttitle, parse_posts) VALUES (%s, %s, %s, %s)"
		selquery = "SELECT * FROM cjposts WHERE `posturl` = %s AND `posttitle` = %s"
		
	def __init__(self):
		self.setupDBCon()
	
	def __del__(self):
		self.conn.close()
	
	def setupDBCon(self):
		self.conn = MySQLdb.connect(host='localhost', user='admin', passwd='admin', db='craigslistdb')
		self.curr = self.conn.cursor()

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
		self.curr.execute(self.selquery, (item['posturl'], item['posttitle']))
		if self.curr.fetchone() is None:
			self.curr.execute(self.query, (item['posturl'], item['time'], item['posttitle'], item['parse_posts']))
			self.conn.commit()
		return item
	
