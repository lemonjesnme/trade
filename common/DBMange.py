# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import pymysql
import time

class DBMange(object):
    
     def __init__(self):
         
         self.db = pymysql.connect("localhost","root","root","stock",charset="utf8")
         self.cursor = self.db.cursor()  
         
     def select(self,sql):
      self.cursor.execute(sql)
      # 获取所有记录列表
      self.results = self.cursor.fetchall()
      return self.results