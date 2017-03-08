# -*- coding: utf-8 -*-

# Scrapy settings for cjscrap project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'cjscrap'

SPIDER_MODULES = ['cjscrap.spiders']
NEWSPIDER_MODULE = 'cjscrap.spiders'

USER_AGENT_LIST = "useragents.txt"

ROTATING_PROXY_LIST = [
	'83.239.58.162:8080',
	'189.39.123.185:80',
	'36.81.184.2:80',
	'36.81.185.233:80',
	'67.205.143.252:8080',
	'190.248.128.122:3128',
	'36.81.184.4:80',
	'124.124.1.178:3128',
	'94.177.233.39:3128',
	'142.4.195.59:3128',
	'36.81.184.111:80',
	'36.81.184.149:80',
	'36.81.184.239:80',
	'36.81.184.242:80',
	'37.187.100.23:3128',
	'122.54.26.3:8080',
	'36.81.184.119:80',
	'36.81.185.96:80',
	'36.81.185.136:80',
	'139.59.109.116:3128',
	'177.12.236.209:80',
	'149.56.147.46:3128',
	'36.81.184.88:80',
	'121.135.146.184:8080',
	'36.81.184.9:80',
	'45.63.14.135:8080',
	'201.16.147.193:80',
	'177.67.82.125:8080',
	'36.82.73.208:80',
	'180.87.192.82:3128',
	'167.160.189.117:3128',
	'36.81.185.73:80',
	'177.12.236.216:80',
	'36.81.185.5:80',
	'158.69.70.35:8080',
	'36.81.184.129:80',
	'217.33.216.114:8080',
	'36.81.184.165:80',
	'36.81.185.2:80',
	'81.47.173.219:3128',
	'36.81.184.152:80',
	'94.177.243.108:3128',
	'212.47.237.198:8000',
	'36.81.184.101:80',
	'36.81.184.45:80',
	'36.81.185.58:80',
	'89.36.220.201:8080',
	'36.73.216.111:80',
	'67.231.241.6:3128',
	'36.81.185.251:80',
	'52.67.89.147:3128',
	'36.81.184.154:80',
	'185.92.221.187:3128',
	'36.81.184.58:80',
	'36.81.185.29:80',
	'36.81.185.180:80',
	'177.54.144.138:8080',
	'36.81.184.20:80',
	'149.56.185.96:8080',
	'89.40.114.83:8080',
	'177.67.82.119:8080',
	'144.217.139.230:8080',
	'51.15.46.137:8080',
	'142.4.210.208:3129',
	'185.107.80.44:3128',
	'189.39.123.176:80',
	'195.13.170.47:8080',
	'36.81.184.23:80',
	'158.69.77.48:8080',
	'54.202.41.204:3128',
	'149.56.250.47:8080',
	'94.177.242.85:8080',
	'36.81.184.46:80',
	'89.46.75.39:80',
	'192.99.98.159:8080',
	'191.96.42.200:8080',
	'195.19.157.195:8080',
	'168.187.239.10:3128',
	'89.38.149.185:8080',
	'78.40.149.240:3128',
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cjscrap (+http://www.yourdomain.com)'
#USER_AGENT = 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY=3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'cjscrap.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'cjscrap.middlewares.MyCustomDownloaderMiddleware': 543,
#}


DOWNLOADER_MIDDLEWARES = {
	'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
	'random_useragent.RandomUserAgentMiddleware': 400,
    #'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    #'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'cjscrap.pipelines.SomePipeline': 300,
#}

ITEM_PIPELINES = {
    'cjscrap.pipelines.CraigsListPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
