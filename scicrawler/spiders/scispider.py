#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

# vi: ft=python:tw=0:ts=4:sw=4

from scrapy.spider import Spider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item
from scrapy.http import FormRequest

class Scispider(Spider):
    name = 'sci'
    start_urls =  [
    'http://apps.webofknowledge.com/WOS_GeneralSearch_input.do?product=WOS&SID=1CZkm6z9VnZxLMnSDVX&search_mode=GeneralSearch']
    
    def parse(self,response):
        sel = Selector(response)
        print '*********************',sel.xpath('//title/text()').extract(),'***********************'

        yield  FormRequest(
       # url="http://apps.webofknowledge.com/WOS_GeneralSearch_input.do?product=WOS&SID=1CZkm6z9VnZxLMnSDVX&search_mode=GeneralSearch",
        url = "http://apps.webofknowledge.com/WOS_GeneralSearch.do",
        formdata = {
            'SID':'1CZkm6z9VnZxLMnSDVX',
            'action':'search',
            'editions':'SCI',
            'endYear':'2014',
            'fieldCount':'1',
            'limitStatus':'expanded',
            'max_field_count':'25',
            'period':'Year Range',
            'product':'WOS',
            'range':'ALL',
            'sa_params':"WOS||1CZkm6z9VnZxLMnSDVX|http://apps.webofknowledge.com|",
            'search_mode':'GeneralSearch',
            'ssStatus':'display:none',
            'ss_lemmatization':'On',
            'startYear':'2011',
            'value(input1)':'sheng XQ',
            'value(select1)':'AU'},
            callback = self.after_post)

    def after_post(self,response):
        sel = Selector(response)
        print '22222*****'
        #print sel.xpath("//div[@class='search-results']").extract()
        print sel.xpath("//title/text()").extract()
        
