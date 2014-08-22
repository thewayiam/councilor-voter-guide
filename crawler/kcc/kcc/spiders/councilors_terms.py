# -*- coding: utf-8 -*-
import re
import urllib
from urlparse import urljoin
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from kcc.items import Councilor


def GetDate(text):
    matchTerm = re.search(u'''
        (?P<year>[\d]+)[\s]*(年|[.])[\s]*
        (?P<month>[\d]+)[\s]*(月|[.])[\s]*
        (?P<day>[\d]+)
    ''', text, re.X)
    if matchTerm:
        return '%04d-%02d-%02d' % (int(matchTerm.group('year'))+1911, int(matchTerm.group('month')), int(matchTerm.group('day')))
    else:
        return None

class Spider(scrapy.Spider):
    name = "councilors_terms"
    allowed_domains = ["www.kcc.gov.tw"]
    start_urls = ["http://www.kcc.gov.tw/PeriodMembers/Search.aspx",]
    download_delay = 0.5

    def start_requests(self):
        payload = {
            '__EVENTTARGET':'ctl00$ContentPlaceHolder1$ddlPeriodTerms',
            '__EVENTARGUMENT':'',
            '__LASTFOCUS':'',
            '__VIEWSTATE':u'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',
            'ctl00$txtSearch':u'全文檢索',
            'ctl00$hidSelectNode':u'1287/1293',
            'ctl00$ContentPlaceHolder1$ddlPeriod':'7',
            'ctl00$ContentPlaceHolder1$ddlPeriodTerms':'36',
            'ctl00$ContentPlaceHolder1$txtName':u'姓名及關鍵字',
            'ctl00$ContentPlaceHolder1$hidName':'',
            'ctl00$ContentPlaceHolder1$btnSearch.x':'33',
            'ctl00$ContentPlaceHolder1$btnSearch.y':'14'
        }
        return [FormRequest("http://www.kcc.gov.tw/PeriodMembers/Search.aspx", formdata=payload, callback=self.parse)]

    def parse(self, response):
        sel = Selector(response)
        nodes = sel.xpath('//table/tr/td/span/a[contains(@href, "Introduction.aspx?KeyID")]')
        for node in nodes:
            yield Request('http://www.kcc.gov.tw/PeriodMembers/%s' % node.xpath('@href').extract()[0], callback=self.parse_profile)

    def parse_profile(self, response):
        sel = Selector(response)
        item = Councilor()
        item['election_year'] = '2010'
        item['county'] = '高雄市'
        image = sel.xpath('//div/img[@id="ContentPlaceHolder1_lv_Pic_0"]/@src').extract()[0]
        item['image'] = urljoin(response.url, urllib.quote(image.encode('utf8')))
        header = sel.xpath('//div[@class="info_data"]/table/tr/td/h4/text()').re(u'(.*?)(議員|副議長|議長)')
        item['name'] = re.sub(u'\(.*\)', '', header[0])
        item['title'] = header[1]
        item['in_office'] = True
        item['term_start'] = '%s-12-25' % item['election_year']
        item['term_end'] = {'date': '2014-12-25'}
        item['contact_details'] = []
        item['links'] = [{'url': response.url, 'note': u'議會個人官網'}]
        nodes = sel.xpath('//table/tr/td')
        for node in nodes:
            th = node.xpath('preceding-sibling::th[1]/text()').extract()
            if th:
                th = re.sub(u'[\s:　]', '', th[0])
            else:
                continue
            if re.search(u'性別', th):
                item['gender'] = node.xpath('text()').extract()[0]
            if re.search(u'所屬政黨', th):
                item['party'] = node.xpath('table/tr/td/text()').extract()[0]
            if re.search(u'聯絡電話', th):
                for phone in [re.sub(u'\s', '', x) for x in node.xpath('text()').extract()]:
                    item['contact_details'].append({'type': 'voice', 'label': u'傳真', 'value': phone})
            if re.search(u'傳真電話', th):
                for phone in [re.sub(u'\s', '', x) for x in node.xpath('text()').extract()]:
                    item['contact_details'].append({'type': 'fax', 'label': u'傳真', 'value': phone})
            if re.search(u'電子郵件', th):
                for email in [re.sub(u'\s', '', x) for x in node.xpath('a/text()').extract()]:
                    item['contact_details'].append({'type': 'email', 'label': u'電子信箱', 'value': email})
            if re.search(u'通訊地址', th):
                for address in [re.sub(u'\s', '', x) for x in node.xpath('text()').extract()]:
                    item['contact_details'].append({'type': 'address', 'label': u'通訊處', 'value': address})
            if re.search(u'學歷', th):
                item['education'] = [re.sub(u'\s', '', x) for x in node.xpath('ul/text()').extract()]
            if re.search(u'經歷', th):
                item['experience'] = [re.sub(u'\s', '', x) for x in node.xpath('ul/text()').extract()]
            if re.search(u'備註', th):
                item['remark'] = node.xpath('span/font/text()').extract()
                if item['remark']:
                    item['term_end'] = {}
                    item['term_end']['date'] = GetDate(node.xpath('span/font/text()').extract()[0])
                    item['term_end']['reason'] = ''
                    item['in_office'] = False
            if re.search(u'服務政見', th):
                item['platform'] = [re.sub(u'\s', '', x) for x in node.xpath('ol/text()').extract()]
        return item
