# -*- coding: utf-8 -*-


from VK_CODE import VK_CODE
#from pywinauto import application
#import win32clipboard as wc
from pykeyboard import PyKeyboard
import win32gui, win32api, win32con 
import time



class Software(object):
   
    def __init__(self,keyword):
        self.k = PyKeyboard() #get pykeyboard        
        self.software=keyword
        self.hWndChildList=0
        self.para_hld=win32gui.FindWindow(None,self.software)
        if self.IsWindow():
            self.hWndChildList=self.demo_child_windows(self.para_hld) #get hld 
            attr=self.show_window_attr(self.para_hld)
            win32api.SetCursorPos([attr['post'][0],attr['post'][1]]) #Mover to post(x,y)
			
    '''
    判定窗口是否激活
    '''    
    def IsWindow(self):
        if self.para_hld>0:
           return 1;
        else:
           return 0;
           
    '''
    窗口置顶
    '''
    def topWindow(self):
        self.Key_event('ctrl')
        win32gui.SetForegroundWindow(self.para_hld)  #show window
        
    '''
    输入键盘事件
    '''
    def keyStr(self,st):
        self.k.type_string(st)
        
    '''
    输入键盘事件
    '''
    def Key_event(self,key):
        win32api.keybd_event(VK_CODE[key],0,0,0) #
        win32api.keybd_event(VK_CODE[key],0,win32con.KEYEVENTF_KEYUP,0) #
        
    '''
    ldList:
    'post:?§|left, top, right, bottom  
    '''
    def GetHld(self,post):
        for hld in self.hWndChildList:
            left, top, right, bottom =win32gui.GetWindowRect(hld) #get hld post left top right bottom
            #if (post[0]==left) & (post[1]==top) & (post[2]==right) & (post[3]==right):
            if (post[0]==left) & (post[1]==top): #get hld by (x,y) left top
                 return hld
        return 0
        
    '''
    通过字符找到窗口
    '''
    def GetHldWord(self,word):
        for hld in self.hWndChildList:
            title = win32gui.GetWindowText(hld) 
            title=title.decode('gbk')
            if title==word:
                 return hld
        return 0
    
    '''
    获取窗口下的所有子窗口
    '''
    def demo_child_windows(self,parent):  
        if not parent:  
            return   
        hWndChildList = []  
        win32gui.EnumChildWindows(parent, lambda hWnd, param: param.append(hWnd),  hWndChildList)  
        return hWndChildList  
    
    #get all hld attr
    def show_window_attr(self,hWnd):  
        if not hWnd:  
            return  
       
        title = win32gui.GetWindowText(hWnd)  
        clsname = win32gui.GetClassName(hWnd) 
        left, top, right, bottom =win32gui.GetWindowRect(hWnd) #
        attr = {'hWnd':hWnd,'title': title, 'clsname':clsname, 'post':[left,top,right,bottom]}    
    
        return attr 
        


