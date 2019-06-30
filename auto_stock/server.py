# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 10:04:22 2018

@author: daveqing
@qq    : 1029329095
"""

from bottle   import route, run, request,response
from auto  import Auto 

#解决跨域的问题    
def allow_cross_domain(fn):  
    def _enable_cors(*args, **kwargs):  
        #set cross headers  
        response.headers['Access-Control-Allow-Origin'] = '*'  
        response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,OPTIONS'  
        allow_headers = 'Referer, Accept, Origin, User-Agent'  
        response.headers['Access-Control-Allow-Headers'] = allow_headers       
        if request.method != 'OPTIONS':  
            # actual request; reply with the actual response  
            return fn(*args, **kwargs)      
    return _enable_cors  

@route('/')
@allow_cross_domain 
def index():
       
    return '欢迎使用本软件0.0.2 <br> 提醒：启动本软件前，请先启动同花顺独立交易软件，不要同时开启行情软件<br>增加提醒启动软件的功能 <br>增加查询帐户资金的功能'

@route('/buy', methods=['GET', 'POST'])
@allow_cross_domain   
def buy():
    stock = request.GET.get('stock','').strip() 
    price = request.GET.get('price','').strip() 
    num = request.GET.get('num','').strip()
    auto.buy(stock,price,num);
    print {"srock":stock,"price":price,"num":num}
   
    return {"srock":stock,"price":price,"num":num}
    
@route('/sell', methods=['GET', 'POST'])
@allow_cross_domain             
def sell():
    stock = request.GET.get('stock','').strip() 
    price = request.GET.get('price','').strip() 
    num = request.GET.get('num','').strip()
    auto.sell(stock,price,num);
    print {"srock":stock,"price":price,"num":num}
   
    return {"srock":stock,"price":price,"num":num}
    
@route('/getAllInfo', methods=['GET', 'POST'])
@allow_cross_domain             
def getAllInfo():
    return auto.getAllInfo();

@route('/test', methods=['GET', 'POST'])
@allow_cross_domain 
def test():
    auto.topWindow()
    return '进行测试中'
    
def start():     
    run(host='0.0.0.0', port=8889, debug=True)

auto = Auto()

#start()
      
    
    
    
    