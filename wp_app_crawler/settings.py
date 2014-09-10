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

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wp_app_crawler (+http://www.yourdomain.com)'
