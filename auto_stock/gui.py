# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 22:19:50 2018

@author: daveqing
@qq    : 1029329095
"""

from Tkinter import Frame,Label,Button,Tk
import tkinter.messagebox #这个是消息框，对话框的关键 
from auto  import Auto 
from server import start
from webbrowser  import   open
#from lib   import Job
import threading

class App:  
    def __init__(self, master):  
        #构造函数里传入一个父组件(master),创建一个Frame组件并显示  
        frame = Frame(master) 
        master.geometry('300x50')
        frame.pack()  
        #创建两个button，并作为frame的一部分  
        self.urlpLabel= Label(frame,text=u"服务器地址：127.0.0.0:8889")
        self.urlpLabel.grid(row=1,column=0)  
        #sf_text = StringVar()
        self.button = Button(frame, text=u"启动", fg="red", command=self.start)  
        #此处side为LEFT表示将其放置 到frame剩余空间的最左方 
        self.button.grid(row=1,column=2) 
           
        self.button = Button(frame, text=u"停止", fg="red", command=self.stop)  
        #此处side为LEFT表示将其放置 到frame剩余空间的最左方
        self.button.grid(row=1,column=3) 
        self.button = Button(frame, text=u"打开浏览器", fg="red", command=self.openBrow)  
        #此处side为LEFT表示将其放置 到frame剩余空间的最左方
        self.button.grid(row=1,column=4) 
    
    def start(self):
        auto = Auto()
        if auto.IsWindow():
           t = threading
           t = threading.Thread(target=start, name='LoopThread')
           t.start()
           open("http://127.0.0.1:8889")
        else:
           tkinter.messagebox.showinfo('提示','请先启动同花顺交易软件')
      
    def stop(self):
        print '关闭程序成功'
    
    def openBrow(self):
        open("http://127.0.0.1:8889")
        
win = Tk()  
app = App(win) 
win.mainloop()