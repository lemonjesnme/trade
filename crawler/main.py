# -*- coding: utf-8 -*-

# 爬虫启动入口

#from manager import Manager
from downloader import download
from parsers import Parser
from processor import Processor
import json
import re

class Crawler(object):

    def __init__(self):
        self.pres = Parser()
        self.proc = Processor()
       
    def start(self):
        """
        启动爬虫方法
        :param urls: 启动URL
        :return: 抓取的URL数量
        """

        self.getHy()
        self.getStockLHRank(2)
    #获取数据东方财富买入最多的股票。1小时
    def getStockLHRank(self,timePeriod):
         root_urls = 'https://simqry2.eastmoney.com/qry_tzzh_v2?type=spo_rank_tiger&plat=2&ver=web20&rankType=30001&timePeriod='+str(timePeriod)+'&recIdx=1&recCnt=50'
         html = download(root_urls,'utf8')      
         print html
         data = self.pres.StockLHRank(html)
         self.proc.StockLHRank(data)
         #print data
         #print data[0]

    #https://simqry2.eastmoney.com/qry_tzzh_v2?type=spo_rank_tiger&plat=2&ver=web20&rankType=30001&timePeriod=3&recIdx=1&recCnt=50
        
    #获取行业资金流入情况 
    def getHy(self):
        for p in range(1,3):
            root_urls = 'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?cmd=C._BKHY&type=ct&st=BalFlowMain&sr=-1&p='+str(p)+'&token=894050c76af8597a853f5b408b759f5d&sty=DCFFITABK&rt=51115543'
            html = download(root_urls,'utf8')
            '''
            html =re.findall(r'[(](.*?)[)]', html) 
            jsonObj  = json.loads(html[0])
            print   jsonObj[0].split(',')[14]
            '''
            data = self.pres.easey(html)
            self.proc.hyDb(data)
        
  

if __name__ == "__main__":
    crawler = Crawler()
    crawler.start()
    

   
    #for index in range(len(jsonObj)):
    #    print jsonObj[index].split(',')[2]
    #print jso[1]
    #print html
    #with open('test5.html','w') as f:
    #    f.write(html[0].encode('utf-8'))
        
    #html.decode('gb2312')
    
    #nums = crawler.start(root_urls)
   
    #print('爬虫执行完成，共抓取{}个URL'.format(nums))
