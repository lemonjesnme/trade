# -*- coding: utf-8 -*-
import pymysql
import time

class Processor(object):

    #print len(jsonObj)
   def StockLHRank(self,date):
        db = pymysql.connect("localhost","root","root","stock",charset="utf8")
        cursor = db.cursor()    
        for index in range(len(date)):
            price = date[index]['price']
            avgBuyPrice = date[index]['avgBuyPrice']
            zuheBuyIn = date[index]['zuheBuyIn']
            stkCode= date[index]['stkCode']
            stkName = date[index]['stkName']
            prcPcnt = date[index]['prcPcnt']
            newtime = time.strftime("%Y-%m-%d", time.localtime())
            sql = "INSERT INTO `stocklhrank` (`price`,`avgBuyPrice`,`zuheBuyIn`,`stkCode`,`stkName`,`prcPcnt`,`newtime`)VALUES\
        ('%s','%s','%s','%s','%s','%s','%s')"% \
        (price,avgBuyPrice,zuheBuyIn,stkCode,stkName,prcPcnt,newtime);
            cursor.execute(sql)
            db.commit()
        db.close()
            
   
   def hyDb(self,date):
        db = pymysql.connect("localhost","root","root","stock",charset="utf8")
        cursor = db.cursor()    
        for index in range(len(date)):
            tmp = date[index].split(',')
            newtime = time.strftime("%Y-%m-%d", time.localtime())
            hy_code = tmp[1]
            hy_name = tmp[2]
            hy_increase = tmp[3]
            hy_zyamount = tmp[4]
            hy_zyjzb = tmp[5]
            hy_cdamount = tmp[6]
            hy_cdjzb = tmp[7]
            hy_ddamount = tmp[8]
            hy_ddjzb = tmp[9]
            hy_zdamount = tmp[10]
            hy_zdjzb = tmp[11]
            hy_sdamount = tmp[12]
            hy_sdjzb = tmp[13]
            hy_zystockname = tmp[14]
            hy_zystock = tmp[15]
            #print hy_code
           
            sql = "INSERT INTO `hy` (`newtime`,`hy_code`,`hy_name`,`hy_increase`,`hy_zyamount`,`hy_zyjzb`,`hy_cdamount`,`hy_cdjzb`,`hy_ddamount`,`hy_ddjzb`,`hy_zdamount`,`hy_zdjzb`,`hy_sdamount`,`hy_sdjzb`,hy_zystockname,`hy_zystock`)VALUES\
        ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"% \
        (newtime,hy_code,hy_name,hy_increase,hy_zyamount,hy_zyjzb,hy_cdamount,hy_cdjzb,hy_ddamount,hy_ddjzb,hy_zdamount,hy_zdjzb,hy_sdamount,hy_sdjzb,hy_zystockname,hy_zystock);
            cursor.execute(sql)
            db.commit()
        db.close()
        