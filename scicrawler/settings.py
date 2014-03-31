# Scrapy settings for scicrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scicrawler'

SPIDER_MODULES = ['scicrawler.spiders']
NEWSPIDER_MODULE = 'scicrawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scicrawler (+http://www.yourdomain.com)'
'''
USER_AGENT = 'Mozilla/5.0 (compatible; iaskspider/1.0; MSIE 9.0)'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': 400,
    'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': 700,
}

DOWNLOAD_DELAY = 0.25
RANDOMIZE_DOWNLOAD_DELAY = True

COOKIES_ENABLED = True
COOKIES_DEBUG = True
'''
ITEM_PIPELINES = {'scicrawler.pipelines.CSVPipeline': 300 }
