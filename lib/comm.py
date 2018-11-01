# -*- coding: gb2312 -*- 



def writTxt(fileName,data):
    txt = open(fileName,'a')
    txt.write(data)
    txt.write('\n')
    txt.close()
    
def writU(text):
    print (text)

def gbk2utf8(s):  
    return s.decode('gbk').encode('utf-8')

