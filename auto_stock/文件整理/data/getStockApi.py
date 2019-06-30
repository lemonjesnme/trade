# -*- coding: utf-8 -*-
'''
获取股票数据
'''
import urllib2
import json 
import numpy as np
import pandas as pd
import tushare as ts
import datetime
import os
import re
import json
import demjson

class StockData:
    
    def __init__(self,stock):
        self.stock     = stock
        #self.hist_data = ts.get_hist_data(self.stock,start=statTime)
        #self.hist_data = self.hist_data.sort_index()
    
    #返回实时数据
    def getTodayData(self):
        st = self.getStockType( self.stock)+ self.stock
        url='http://hq.sinajs.cn/list='+st
        return self.toolGet(url).split(',')
        
    
    #http请求获取数据
    def toolGet(self,url):
      result=urllib2.urlopen(url).read()
      #print result
      return result
     #返回历史数据
      
    #返回60分钟图
    #https://ex.sina.com.cn/quotes_service/api/jsonp_v2.php/c/CN_MarketData.getKLineData?symbol=sh600482&scale=60&ma=no&datalen=1023
      
    def getH60(self):
        paran = self.getStockType( self.stock)+ self.stock
        url = 'https://ex.sina.com.cn/quotes_service/api/jsonp_v2.php/c/CN_MarketData.getKLineData?symbol='+paran+'&scale=60&ma=no&datalen=1023'
        statData = self.toolGet(url)
        statData =re.findall(r'[(](.*?)[)]', statData)  
        #print statData[0]
        statData =demjson.decode(statData[0])
        return statData
 
       
    def get_hist(self,num):
        if num>100 or num<2:
            print '不能超过100或者不能小过2'
        paran = self.getStockType( self.stock)+ self.stock
        url = 'http://data.gtimg.cn/flashdata/hushen/latest/daily/'+paran+'.js?maxage=10&visitDstTime=1'
        #http://data.gtimg.cn/flashdata/hushen/latest/daily/sz000002.js?maxage=10&visitDstTime=1
        statData = self.toolGet(url).split(',')[0].split('\\\n')     
        lent = len(statData)-1
        data = []
        for i in range(num,lent):
            data.append(statData[i].split(' '))
        return data
        #return data1.to_json(orient='split')
    '''
    获取历史数据
    '''
    def get_hist_k(self):
        data1      =self.hist_data[['open','close','high','close']]
        inde       =list(data1.index)
        datav      =data1.values
        ma60       =list(np.nan_to_num(self.getMax(60)))
        data       ={'index':inde,'data':datav.tolist(),'ma60':ma60}
        return json.dumps(data)
        #print json.dumps(data)
    #返回成交量
    def get_nun(self):
        nun      = self.hist_data[['volume']]
        nun      = nun.T
        return nun.to_json(orient='split')
        
    #返回均线    
    def getMax(self,date):
        data=[]
        for i in  range(len(self.hist_data['close'])):
            data_ma    = [self.hist_data['close'][-(date-i):i+1]]
            #print np.mean(x60)
            data.append(np.mean(data_ma))
        return data
        
    #获取收盘价
    def get_clos(self):
         
        data1      =self.hist_data[['close']]
        data1      = data1.T
       
        return data1.to_json(orient='split')
        
    #涨跌幅
    def get_change(self):
         data2       =self.hist_data[['p_change']]
         data2      = data2.T
         return data2.to_json(orient='split')
         
    #换手率   
    def get_turnover(self):
         data2       =self.hist_data[['turnover']]
         
         return data2.to_json(orient='split')
     
    #返回净利润
    def get_net_profits(self):
        
        data     = pd.read_json('profit_data/20170103.json')
        data     = data[data.code==int(self.stock)]
        profitss =data['net_profits'].values
        dates    =data['date'].values
        data = {'profitss':profitss.tolist(),'dates':dates.tolist()}
        return json.dumps(data)
    
    
    #获取行情数据
    def get_all(self):
        now      = datetime.datetime.now()
        n        = now.strftime('%Y-%m-%d')
        filename = 'nowdata/'+str(n)+'.json'
        print(filename)
        if(os.path.exists(filename)):
            data = pd.read_json(filename)
            data = data[['code','name','changepercent']]
        else:
            data  = ts.get_today_all()
            data.to_json(filename,orient='records')
            
      
        return data.to_json(orient='split')  
    # 股票类型判断  
    def getStockType(self,stock):
        st = stock[0:3]
        if st=='000' or st=='300':
            return 'sz'
        #600开头的股票是上证A股    
        if st=='600' or st=='601' or st=='603':
            return 'sh'
        #typeList = ['600','601','603']
#g = StockData('600482')
#print g.get_hist(97)
#data = ts.get_hist_data('002487',start='2018-07-01')
#print data.getTodayData()
#data = StockData('000651')
#d =  data.get_hist()
#print d
#print d[0].split('\\\n')[6].split(' ')

#stockData =  data.get_hist()
#print stockData
#print stockData[3] 
#print GetTabName('GET')
'''
    0：”大秦铁路”，股票名字； 
    1：”27.55″，今日开盘价； 
    2：”27.25″，昨日收盘价； 
    3：”26.91″，当前价格； 
    4：”27.55″，今日最高价； 
    5：”26.20″，今日最低价； 
    6：”26.91″，竞买价，即“买一”报价； 
    7：”26.92″，竞卖价，即“卖一”报价； 
    8：”22114263″，成交的股票数，由于股票交易以一百股为基本单位，所以在使用时，通常把该值除以一百； 
    9：”589824680″，成交金额，单位为“元”，为了一目了然，通常以“万元”为成交金额的单位，所以通常把该值除以一万； 
    10：”4695″，“买一”申请4695股，即47手； 
    11：”26.91″，“买一”报价； 
    12：”57590″，“买二” 
    13：”26.90″，“买二” 
    14：”14700″，“买三” 
    15：”26.89″，“买三” 
    16：”14300″，“买四” 
    17：”26.88″，“买四” 
    18：”15100″，“买五” 
    19：”26.87″，“买五” 
    20：”3100″，“卖一”申报3100股，即31手； 
    21：”26.92″，“卖一”报价
    (22, 23), (24, 25), (26,27), (28, 29)分别为“卖二”至“卖四的情况” 
    30：”2008-01-11″，日期； 31：”15:05:32″，时间；
'''