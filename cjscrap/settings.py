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
	'47.52.117.173:80',
	'36.85.78.241:8080',
	'203.146.82.253:3128',
	'24.42.167.242:3128',
	'165.227.53.107:3128',
	'47.89.41.164:80',
	'104.196.123.46:80',
	'61.7.190.68:3128',
	'203.74.4.1:80',
	'35.196.236.101:80',
	'116.58.224.195:52136',
	'202.70.83.251:8080',
	'198.50.219.232:8080',
	'182.23.49.19:8080',
	'91.191.173.37:808',
	'202.159.36.70:80',
	'203.74.4.0:80',
	'37.29.82.115:65103',
	'189.206.107.6:8080',
	'45.6.216.66:3128',
	'103.66.199.204:8080',
	'208.83.106.105:9999',
	'35.196.204.41:80',
	'35.196.126.44:80',
	'89.22.52.3:53281',
	'35.199.120.22:80',
	'118.69.57.180:53281',
	'35.196.232.41:80',
	'163.172.28.22:80',
	'89.236.17.106:3128',
	'191.102.85.234:8080',
	'197.232.17.83:8080',
	'83.174.63.181:80',
	'218.50.2.102:8080',
	'115.79.43.156:8888',
	'52.29.142.253:3128',
	'46.229.139.247:8080',
	'35.196.226.97:80',
	'51.15.51.142:3128',
	'94.103.24.145:80',
	'188.0.226.248:53281',
	'203.74.4.3:80',
	'203.74.4.4:80',
	'181.214.224.96:3128',
	'35.196.221.191:80',
	'119.42.70.245:52225',
	'203.74.4.5:80',
	'195.181.223.66:3128',
	'35.202.22.18:80',
	'104.152.189.90:80',
	'36.75.255.225:80',
	'223.30.74.213:80',
	'104.196.182.17:80',
	'110.78.150.139:52136',
	'208.139.7.6:80',
	'110.171.227.106:3128',
	'220.100.130.121:8080',
	'197.245.217.85:52136',
	'104.198.26.242:80',
	'203.74.4.7:80',
	'188.0.168.205:8080',
	'36.67.87.217:52136',
	'35.196.160.131:80',
	'137.74.254.242:3128',
	'35.196.90.170:80',
	'186.47.46.6:65103',
	'52.221.244.122:80',
	'47.88.32.46:3128',
	'213.136.89.121:80',
	'35.196.21.26:80',
	'213.136.77.246:80',
	'162.223.91.18:3128',
	'203.58.117.34:80',
	'203.74.4.2:80',
	'05.135.195.166:3128',
	'52.174.156.96:3128',
	'190.1.174.38:53281',
	'54.36.182.96:3128',
	'80.83.20.14:80',
	'35.196.200.109:80',
	'143.0.188.213:80',
	'178.238.40.33:80',
	'196.40.117.114:8000',
	'203.74.4.6:80',
	'103.85.192.54:62744',
	'176.15.163.199:53281',
	'185.64.208.49:53281',
	'47.52.70.195:80',
	'118.69.140.108:53281',
	'36.67.114.226:62225',
	'190.0.0.174:8080',
	'118.69.61.57:8888',
	'210.212.73.61:80',
	'125.21.255.50:52136',
	'74.94.80.101:53281',
	'213.13.171.123:8080',
	'223.207.92.5:8080',
	'223.19.206.178:8380',
	'47.91.235.15:80',
	'116.58.253.224:52136',
	'61.7.186.144:52136',
	'166.78.179.49:80',
	'186.92.106.207:8080',
	'74.83.246.105:8081',
	'81.192.184.214:3128',
	'125.24.135.49:8080',
	'190.199.218.189:8080',
	'190.74.205.140:8080',
	'167.114.250.199:9999',
	'213.24.60.52:8080',
	'93.184.160.246:8080',
	'189.85.29.98:8080',
	'181.209.70.170:8082',
	'132.255.73.243:8080',
	'114.44.186.39:8080',
	'110.170.150.179:8080',
	'103.58.75.42:8080',
	'103.19.131.201:53281',
	'212.126.110.196:8080',
	'36.67.16.209:53281',
	'203.76.223.113:8080',
	'128.75.161.176:9999',
	'87.249.205.103:8080',
	'182.253.72.107:8080',
	'112.140.184.139:3129',
	'167.114.47.231:3128',
	'78.26.207.173:53281',
	'178.62.72.97:8118',
	'91.194.247.250:8085',
	'35.196.238.161:80',
	'94.237.38.88:80',
	'178.238.231.201:3128',
	'222.124.152.138:80',
	'165.90.243.26:52225',
	'163.172.217.103:3128',
	'181.112.61.162:65103',
	'195.98.68.176:53281',
	'149.255.154.4:8080'
]
HTTPS_PROXIES = [
	'178.238.40.34:80',
	'212.232.60.219:3128',
	'79.170.152.107:53281',
	'190.14.213.26:65103',
	'109.121.161.192:53281',
	'91.191.184.34:5358',
	'171.101.236.116:3128',
	'82.78.152.253:8080',
	'80.89.133.210:3128',
	'203.76.113.226:80',
	'115.70.186.106:8080',
	'103.43.149.154:80',
	'200.122.211.26:8080',
	'201.19.187.67:8080',
	'179.189.236.197:53281',
	'183.88.21.198:8080',
	'196.61.27.58:53281',
	'218.166.129.155:53281',
	'164.77.134.10:8080',
	'201.217.246.34:8080',
	'41.60.237.78:52335',
	'200.109.119.126:63909'
]


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cjscrap (+http://www.yourdomain.com)'
#USER_AGENT = 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS=5

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
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
    'scrapy_rotated_proxy.downloadmiddlewares.proxy.RotatedProxyMiddleware': 750,
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
