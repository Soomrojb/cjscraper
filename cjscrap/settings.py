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


# -----------------------------------------------------------------------------
# ROTATED PROXY SETTINGS (Spider Settings Backend)
# -----------------------------------------------------------------------------
#DOWNLOADER_MIDDLEWARES.update({
    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
    #'scrapy_rotated_proxy.downloadmiddlewares.proxy.RotatedProxyMiddleware': 750,
#`})
ROTATED_PROXY_ENABLED = True
PROXY_STORAGE = 'scrapy_rotated_proxy.extensions.file_storage.FileProxyStorage'
# When set PROXY_FILE_PATH='', scrapy-rotated-proxy
# will use proxy in Spider Settings default.
PROXY_FILE_PATH = ''
HTTP_PROXIES = [
'159.192.232.200:55555',
'35.196.39.157:8080',
'124.120.75.203:8080',
'179.95.37.79:8080',
'94.177.175.232:3128',
'177.131.16.158:8081',
'52.224.181.154:3128',
'13.126.222.242:80',
'58.26.10.67:8080',
'13.115.180.145:8080',
'128.199.236.22:3128',
'173.212.202.65:443',
'165.227.228.78:80',
'149.255.154.4:8080',
'5.189.133.231:80',
'69.27.184.131:53281',
'103.205.59.140:62947'
]
HTTPS_PROXIES = [
'150.95.184.254:3128',
'93.104.211.232:808',
'180.254.192.228:9000',
'52.68.207.46:8080',
'213.44.87.247:8080',
'52.197.37.22:8080',
'103.43.149.151:80',
'208.163.39.218:8118'
]


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cjscrap (+http://www.yourdomain.com)'
#USER_AGENT = 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS=500

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
    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
    #'scrapy_rotated_proxy.downloadmiddlewares.proxy.RotatedProxyMiddleware': 450,
	#'random_useragent.RandomUserAgentMiddleware': 400,
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
