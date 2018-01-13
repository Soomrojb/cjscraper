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

# Rotating Proxy Settings
ROTATING_PROXY_LIST_PATH = 'proxylist.txt'
ROTATING_PROXY_LOGSTATS_INTERVAL = 1
ROTATING_PROXY_BACKOFF_CAP = 7200
ROTATING_PROXY_PAGE_RETRY_TIMES = 20
ROTATING_PROXY_BACKOFF_BASE = 5
DOWNLOADER_MIDDLEWARES = {
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cjscrap (+http://www.yourdomain.com)'
#USER_AGENT = 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS=200

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
