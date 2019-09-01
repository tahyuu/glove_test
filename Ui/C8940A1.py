#-*- coding:utf-8 -*-
import os
from ctypes import *
import time

###################################################
### Fuction List
### 1, Go to Positions
### 2, Return Zero.
### 3, Init 8940A
### 4, How to Stop
### question.  can z axis return zero? -300 ok？
###            
###################################################

class C8940A1:
    def __init__(self):
        #self.CObjdll = cdll.LoadLibrary("8940A1.dll")
        self.WObjdll = windll.LoadLibrary("8940A1.dll")
        cardno = self.WObjdll.adt8940a1_initial()
        if cardno<0:
            print "Can't find 8940 Card"
            return -1;
        else:
            pass

    def Set8940A1(self,axis,startv,speed):
        self.WObjdll.set_pulse_mode(0,axis,1,0,0);
        self.WObjdll.set_startv(0,axis,c_int(startv));
        self.WObjdll.set_speed(0,axis,c_int(speed));
    def MoveSingleAxis(self,axis,Steps,Wait=True):
        print axis
        print Steps
        self.WObjdll.pmove(0,axis,Steps);
        x=c_int(0)
        while Wait:
            #print x.value
            self.WObjdll.get_status(0,axis,byref(x));
            if x.value==0:
                break;
    def MoveMultiAxis(self,Xsteps,Ysteps,Wait=True):
        
        self.WObjdll.pmove(0,1,Xsteps);
        self.WObjdll.pmove(0,2,Ysteps);

        s1=c_int(0)
        s2=c_int(0)

        while Wait:
            #print x.value
            self.WObjdll.get_status(0,1,byref(s1));
            self.WObjdll.get_status(0,1,byref(s2));

            if s1.value==0 and s2.value==0 :
                break;

        #print cardno
    def ReturnZero(self):
        pass

    def Stop(self):
        pass
        
    def Start(self):
        c8940a1=C8940A1()
        c8940a1.Set8940A1(1,1000,1000)
        print "Moving to Point 1"
        #c8940a1.MoveSingleAxis(1,100000)
        #time.sleep(5)


        Axislist =[(5000,3000),(1000,0),(1000,0),(1000,0),(1000,0),(1000,0),
                   (-5000,3000),(1000,0),(1000,0),(1000,0),(1000,0),(1000,0),
                   (-5000,3000),(1000,0),(1000,0),(1000,0),(1000,0),(1000,0)]

        for al in Axislist:
            c8940a1.Set8940A1(2,1000,1000)
            c8940a1.Set8940A1(3,50,50)
            #c8940a1.MoveSingleAxis(2,100000)
            #print "Moving to XY"
            c8940a1.MoveMultiAxis(al[0],al[1])
            #print "Moving to Z"
            c8940a1.MoveSingleAxis(3,300,True)
            #return Zero for Z
            c8940a1.MoveSingleAxis(3,-300,True)

        c8940a1.MoveMultiAxis(-10000,-9000,True)


if __name__=="__main__":
    #Init8940A1()
    c8940a1=C8940A1()
    c8940a1.Start()

#cardno = CObjdll.adt8940a1_initial()
#print cardno
#dll = CDLL("8940A1.dll")
