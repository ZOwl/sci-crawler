#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import FormRequest, Request

class SciSpider(CrawlSpider):
    name = 'scispider'
    allowed_domains = ['webofknowledge.com']
    sid = "2BhSeVHTVxUGkfDHX25"
    start_urls = ['http://apps.webofknowledge.com/UA_GeneralSearch_input.do?product=UA&search_mode=GeneralSearch&SID=%s&preferencesSaved=' % sid]

    def parse(self, response):
        print response

# vi: ft=python:tw=0:ts=4:sw=4

