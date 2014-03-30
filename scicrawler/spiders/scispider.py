
# -*- coding: utf-8 -*-

"""

"""

# vi: ft=python:tw=0:ts=4:sw=4

from scrapy.spider import Spider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector,HtmlXPathSelector
from scrapy.item import Item
from scrapy.http import FormRequest,Request
from scicrawler.items import SciItem

class Scispider(Spider):
    name = 'sci'
    sid = '3CJD5w2sc59r712zMpP'
    start_urls =  ['http://apps.webofknowledge.com/WOS_GeneralSearch_input.do?product=WOS&SID=%s&search_mode=GeneralSearch' % sid]
    #start_urls = ['file:///home/geraldyan/Documents/search-results.html']
    papers = []

    def parse(self,response):
        sel = Selector(response)
        print '*********************',sel.xpath('//title/text()').extract(),'***********************'

        return  FormRequest(url = "http://apps.webofknowledge.com/WOS_GeneralSearch.do",
        formdata = {
            'SID':self.sid,
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
        page_count = int(sel.xpath("//span[@id='pageCount.bottom']/text()").extract()[0])
        items = sel.xpath("//div[starts-with(@id,'RECORD_')]")

        for item in items:
            temp = item.xpath(".//a[starts-with(@href,'/full_record')]")
            title = temp.xpath("./value/text()").extract()
            link = temp.xpath("./@href").extract()

            blank = SciItem()
            blank['title'] = title[0]
            blank['link'] = 'http://apps.webofknowledge.com'+link[0]
            self.papers.append(blank)

        for i in range(2,page_count+1):
            yield Request(url = "http://apps.webofknowledge.com/summary.do?product=WOS&parentProduct=WOS&search_mode=GeneralSearch&parentQid=&qid=2&SID=%s&&page=%d" % (self.sid,i),callback = self.pages)    


    def pages(self,response):
        sel = Selector(response)
        items = sel.xpath("//div[starts-with(@id,'RECORD_')]")
        
        for item in items:
            temp = item.xpath(".//a[starts-with(@href,'/full_record')]")
            title = temp.xpath("./value/text()").extract()
            link = temp.xpath("./@href").extract()

            blank = SciItem()
            blank['title'] = title[0]
            blank['link'] = 'http://apps.webofknowledge.com'+link[0]
            self.papers.append(blank)

        for item in self.papers:
            yield Request(url = item['link'],callback=self.detail)
        del self.papers[:]

    def detail(self,response):
        sel = Selector(response)

        title = sel.xpath("//div[@class='title']/value/text()").extract()[0]

        record_blocks = sel.xpath("//div[starts-with(@class,'block-record-info')]")
        #get Authors
        by_ext = record_blocks[0].xpath(".//p[@class='FR_field']/text()").extract()
        del by_ext[0]
        by = ''
        for s in by_ext:
            by += s
        #get Journal
        jou_ext = record_blocks[1].xpath(".//*/text()").extract()
        journal = ''
        for s in jou_ext:
            if s == 'View Journal Information':
                break
            journal += s
        journal = journal.replace('\n\n','linefeed')
        journal = journal.replace('\n',' ')
        journal = journal.replace('linefeed','\n')

        f = open("data.txt",'a')
        f.write(title)
        f.write(journal)
        f.write('&&&\n\n&&&')
        f.close()





