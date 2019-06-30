# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 13:03:14 2018
@author: daveqing
@qq    : 1029329095
"""

from lib import Winauto
import time 
class main():
    
    def __init__(self):
        
         self.wt = Winauto()
         self.statu =   self.wt.SoftwareStat();
         time.sleep(10)
    
    def buy(self,buy_stock,buy_price,buy_nun):
        if self.statu==0:
            return "请先启动交易软件"
        self.wt.BuyS(buy_stock,buy_price,buy_nun)
    
    def sell(self,buy_stock,buy_price,buy_nun):
        if self.statu==0:
            return "请先启动交易软件"
        self.wt.SellS(buy_stock,buy_price,buy_nun)         

#m = main()
#m.buy("002486","0","1000")