# -*- coding: utf-8 -*-


import datetime
import time
from data  import  StockData
from auto  import Auto 

stock = '000735'
proce = '0'
num = '3000'

def doSth():
    auto = Auto()
    data = StockData(stock)
    stockData =  data.getTodayData()
    print stockData[1] #开
    print stockData[3] #最新
    #
    s = round((float(stockData[3])-44.22)/44.22,4)*100
    #if s<1: 
    auto.buy(stock,proce,num)
 
    
    time.sleep(30)
    print '运行成功'
    
    time.sleep(60)

def main(h=0, m=0):
    workTime = range(5)       #make work time [0,1,2,3,4]
    d=datetime.datetime.now() #get now time
    weekday =  d.weekday()    #get week
    while True:
        # determine whether the set time ,such as 0:0
        if weekday in workTime:
            while True:
                now = datetime.datetime.now()
                # The time  up does the thing
                if now.hour==h and now.minute==m:
                    break
                # no time ,sleep 30s
                    '''
                time.sleep(10)
                data = StockData(stock)
                stockData =  data.getTodayData()
                ope = stockData[1]
                new = stockData[3]
                d = round((float(new)-float(ope))/float(ope),4)*100
                print ope
                print new
                print d
                if d>4:
                   auto = Auto()
                   auto.sell(stock,proce,num)
                   break
                   '''
            # do thing ,one day one to make
            
            doSth()

main(h=20,m=44)

