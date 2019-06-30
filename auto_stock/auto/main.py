# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from common import Software
from common import DBMange
import time


class Winauto(object):
   
    def __init__(self):
        self.flush = Software(u'同花顺(v8.60.83) - A股技术分析')
        self.flush.topWindow()
        self.db = DBMange()
    
    def seeK(self,stock):
        self.flush.keyStr(stock)
        self.flush.Key_event('enter')
    
    def getData(self,stype):
        if stype==1:
           sql = "SELECT hy_zystock FROM hy \
               WHERE newtime = '%s'   " % ('2018-08-13')
        if stype==2:
           sql = "SELECT stkCode FROM stocklhrank \
               WHERE newtime = '%s'   " % ('2018-08-13')
        data = self.db.select(sql)
        stock = []
        for row in data:
             fname = row[0]
             # 打印结果
             stock.append(fname)
        return stock
 

auto = Winauto()
stockList =auto.getData(1)
for i in range(len(stockList)):
    auto.seeK(stockList[i][0:6])
    #print stockList[i][0:6]
    time.sleep(5)
