# -*- coding: utf-8 -*-
'''
画分析图用
@author: daveqing
@qq    : 1029329095
'''
from data import StockData   
import matplotlib.pyplot as plt
import json
import numpy as np
from common import DBMange


class Drawing:
    
      def test(self):
         data = [5, 20, 15, 25, 10]
         labels = ['Tom', 'Dick', 'Harry', 'Slim', 'Jim']  
         plt.bar(range(len(data)), data, tick_label=labels)
         plt.show()
      
      def draw_bar(self,labels,quants):
        width = 0.2
        le = len(quants)
        ind = np.linspace(0.5,9.5,le)
        # make a square figure
        fig = plt.figure(1)
        ax  = fig.add_subplot(111)
        # Bar Plot
        ax.bar(ind-width/2,quants,width,color='green')
        # Set the ticks on x-axis
        ax.set_xticks(ind)
        ax.set_xticklabels(labels,rotation=50)
        # labels
        ax.set_xlabel('Country')
        ax.set_ylabel('GDP (Billion US dollar)')
        # title
        #ax.set_title('Top 10 GDP Countries', bbox={'facecolor':'0.8', 'pad':5})
        plt.grid(True)
        plt.show()
        plt.close()
#data = StockData('000651')
#d =  data.get_hist()
#print d

#data  = StockData('600436')
#t = data.get_hist(60)
#data =[]
db = DBMange()
sql = "SELECT hy_name,hy_zyamount FROM hy \
       WHERE hy_code = 'BK0478'   ORDER BY 'hy_increase'"
release = db.select(sql)
print release
'''
for i in t:
    #涨幅=(现价-上一个交易日收盘价）/上一个交易日收盘价*100%
    d = round((float(i[2])-float(i[1]))/float(i[1]),4)*100
    data.append(d)
d = Drawing()
d.draw_bar(data,data)
'''
'''
t = json.loads(t)
data =[]
for i in t['data']:
    print i
    d = round((i[1]-i[0])/i[0],4)*100
    data.append(d)
    
d = Drawing()
d.draw_bar(data,data)
'''
