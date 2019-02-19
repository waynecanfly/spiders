# -*- coding:utf-8 -*-
import re
import urllib2
"""
爬取百度贴吧
"""

class BDTB:
    #初始化，传入基地址
    def __init__(self, baseUrl, seeLZ):
        self.baseUrl = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)
    #获取当前页的代码
    def getPage(self,pageNum):
        try:
            url = 'http://tieba.baidu.com/p/3138733512?see_lz=1&pn=' + str(pageNum)
            # url = self.baseUrl + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            # print response.read()
            return response.read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print u'连接百度贴吧失败，错误原因',e.reason
                return None
    #获取标题
    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h3 class="core_title_txt.*?title="(.*?)".*?class="core_title_btns pull-right">', re.S)
        result = re.search(pattern, page)
        if result:
            # print result.group(1)
            return result.group(1).strip()
        else:
            return None
    # 获取帖子一共有多少页
    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result:
            print result.group(1)
            return result.group(1)
        else:
            return None
if __name__ == '__main__':
    baseUrl = 'http://tieba.baidu.com/p/3138733512?see_lz=1&pn='
    bdtb = BDTB(baseUrl, 1)
    bdtb.getPageNum()



















