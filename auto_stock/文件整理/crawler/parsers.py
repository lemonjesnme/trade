# -*- coding: utf-8 -*-
import datetime
import json
import re

from bs4 import BeautifulSoup



class Parser(object):
 
      def StockLHRank(self,html):
          jsonObj  = json.loads(html)
          data = jsonObj['data']
          return data
     
      '''
      获取当前行业的资金流入
      '''
      def easey(self,html):
        html =re.findall(r'[(](.*?)[)]', html) 
        data  = json.loads(html[0].encode('utf-8'))
        return data
        '''
        html = re.search(r'defjson.*', html, flags=0) 
        html = html.group()
        html = html.split(':')[3].split('}')
        #print html[0]
        jsonObj  = json.loads(html[0].encode('utf-8'))
        return jsonObj
        '''
