#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

# vi: ft=python:tw=0:ts=4:sw=4

from scrapy.spider import Spider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector,HtmlXPathSelector
from scrapy.item import Item
from scrapy.http import FormRequest

class Scispider(Spider):
    name = 'sci'
    sid = '3B5NXihtZmdiwQD5IPw'
    start_urls =  ['http://apps.webofknowledge.com/WOS_GeneralSearch_input.do?product=WOS&SID=%s&search_mode=GeneralSearch' % sid]

    def parse(self,response):
        sel = Selector(response)
        print '*********************',sel.xpath('//title/text()').extract(),'***********************'

        return  FormRequest(url = "http://apps.webofknowledge.com/WOS_GeneralSearch.do",
        formdata = {
            'SID':'3B5NXihtZmdiwQD5IPw',
            'action':'search',
            'editions':['SCI','SSCI','ISTP','ISSHP'],
            'endYear':'2014',
            'fieldCount':'1',
            'limitStatus':'expanded',
            'max_field_count':'25',
            'period':'Year Range',
            'product':'WOS',
            'range':'ALL',
            'sa_params':"WOS||%s|http://apps.webofknowledge.com|" % self.sid,
            'search_mode':'GeneralSearch',
            'ssStatus':'display:none',
            'ss_lemmatization':'On',
            'startYear':'2011',
            'value(input1)':'Sheng XQ',
            'value(select1)':'AU'},
            callback = self.after_post)


    def after_post(self,response):
        sel = Selector(response)
        print '*********************after post*****************************'
        print sel.xpath("//title/text()").extract()
        items = sel.xpath("//div[starts-with(@id,'RECORD_')]")
        for item in items:
            temp = item.xpath(".//a[starts-with(@href,'/full_record')]")
            title = temp.xpath("./value/text()").extract()
            print title[0]
            link = temp.xpath("./@href").extract()
            print link[0]
