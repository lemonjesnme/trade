# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 13:05:36 2018

@author: daveqing
@qq    : 1029329095
"""

from lib import Winauto


#软件启动
class Auto(object):
    
    #软件初始化
    def __init__(self):
        self.Winauto = Winauto();
        
    #判断软件是否启动成功       
    def IsWindow(self):     
      if self.Winauto.IsWindow():
         return 1
      else:
         return 0
        
    #软件启动
    def startApp(self,filePath,var):    
        self.Winauto.appStart(filePath,var)
        
    #购买
    def buy(self,stock,price,num):
        self.Winauto.Buy(stock,price,num)
        
    #出售
    def sell(self,stock,price,num):
        self.Winauto.Sell(stock,price,num)
          
    #查看所有资产
    def getAllInfo(self):
        return self.Winauto.getAllAsset();
    
    #窗口置顶
    def topWindow(self):
        self.Winauto.topWindow()
        
    #查询目前持仓
        

 


    