# coding='utf-8'
import os, sys
import  win32gui,win32con,time,win32api

def Hide_show(flag):
    if flag=="0":
        QQwin = win32gui.FindWindow(u"#32770",u"ADT-8940A1")
        win32gui.ShowWindow(QQwin,win32con.SW_HIDE)
        print QQwin
    elif flag=="1":
        QQwin = win32gui.FindWindow(u"#32770",u"ADT-8940A1")
        win32gui.ShowWindow(QQwin,win32con.SW_SHOW)
        win32gui.SetForegroundWindow(QQwin)
        print QQwin
        


if __name__=="__main__":
    Hide_show(sys.argv[1])
