# -*- coding:utf-8 -*-
import re
import urllib2


class QSBK:
    #初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        self.enable = False
    #传入某一页的索引获得页面代码
    def getPage(self, pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            #构建请求request
            request = urllib2.Request(url, headers=self.headers)
            #利用urlopen获取页面的代码
            response = urllib2.urlopen(request)
            #将页面转化为UTF-8编码
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError, e:
            #判断是否有reason属性
            if hasattr(e, 'reason'):
                print u"连接糗事百科失败，错误原因", e.reason
                return None
    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print '页面加载失败...'
            return None
        pattern = pattern = re.compile('<div class="article.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>', re.S)

