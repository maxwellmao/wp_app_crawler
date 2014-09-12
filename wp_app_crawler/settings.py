# -*- coding: utf-8 -*-

# Scrapy settings for wp_app_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'wp_app_crawler'

SPIDER_MODULES = ['wp_app_crawler.spiders']
NEWSPIDER_MODULE = 'wp_app_crawler.spiders'
COOKIES_ENABLED=False
#DOWNLOAD_DELAY=0.5

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wp_app_crawler (+http://www.yourdomain.com)'
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
    'wp_app_crawler.comm.rotate_useragent.RotateUserAgentMiddleware' :400,
    'wp_app_crawler.comm.proxy.RetryChangeProxyMiddleware': 600
}

DUPEFILTER_CLASS='wp_app_crawler.app_dup_filter.AppURLFilter'
