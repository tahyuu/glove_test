#-*- coding:utf-8 -*-
import os
from ctypes import *
import time
import os

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
        self.WObjdll = cdll.LoadLibrary("8940A1.dll")
        #self.WObjdll = windll.LoadLibrary("8940A1.dll")
        cardno = self.WObjdll.adt8940a1_initial()
        print "aaa %s" %cardno
        if cardno<0:
            print "Can't find 8940 Card"
            return -1;
        else:
            pass
    def Hidden_show(self, status):
        if status==0:
            os.system('return_zero_hidden.bat')
        elif status==1:
            os.system('return_zero_show.bat')


    def InitCard(self):

        ##################
        #open the demo program
        ##################
        program_path="ADT8940A1Demo.exe"
        os.startfile(program_path)
        self.Hidden_show(0)
        #time.sleep(2)
        #os.system('kill_bash.bat')
        #time.sleep(3)
        m_cardno = self.WObjdll.adt8940a1_initial()
        #time.sleep(3)
        for i in range(3):
            
            self.WObjdll.set_limit_mode(m_cardno, i+1, 0, 0, 0);   #//设定限位模式，设正负限位有效，低电平有效
            self.WObjdll.set_command_pos(m_cardno, i+1, 0); # # //清逻辑计数器
            self.WObjdll.set_actual_pos(m_cardno, i+1, 0);         #//清实位计数器
            self.WObjdll.set_startv(m_cardno, i+1, 1000);          #//设定起始速度
            self.WObjdll.set_speed(m_cardno, i+1, 1000);           #//设定驱动速度
            self.WObjdll.set_acc(m_cardno, i+1, 625);               #//设定加速度

    def Set8940A1(self,axis,startv,speed):
        self.WObjdll.set_pulse_mode(0,axis,1,0,0);
        self.WObjdll.set_startv(0,axis,c_int(startv));
        self.WObjdll.set_speed(0,axis,c_int(speed));
    def MoveSingleAxis(self,axis,Steps,Wait=True):
        print axis
        print Steps
        self.WObjdll.pmove(0,axis,Steps);
        x=c_int(1)
        while Wait:
            #print x.value
            self.WObjdll.get_status(0,axis,byref(x));
            if x.value==0:
                break;
    def MoveMultiAxis(self,Xsteps,Ysteps,Wait=True):
        
        self.WObjdll.pmove(0,1,Xsteps);
        self.WObjdll.pmove(0,2,Ysteps);

        s1=c_int(1)
        s2=c_int(1)

        while Wait:
            #print x.value
            self.WObjdll.get_status(0,1,byref(s1));
            self.WObjdll.get_status(0,2,byref(s2));

            if s1.value==0 and s2.value==0 :
                break;

        #print cardno
    def Get_command_pos(self, axis):
        position=c_long(0)
        i=0
        while i<10:
            i=i+1
            self.WObjdll.get_command_pos(0,axis,byref(position));
            if position.value!=0:
                break
        return position.value

    def ReadBit(self, number):
        return self.WObjdll.read_bit(0,number);

    def ReturnZero(self, speed, re_list):
        
        xFlag= re_list[0]
        yFlag= re_list[1]
        zFlag= re_list[2]

        print "spdeed is %s" %speed
        if not re_list[2]:
            retnZ=-1
            retnZ=self.WObjdll.SetHomeMode_Ex(0, 3, 0, 0, 0, -1, 2000, 400, 100)
            retnZ=self.WObjdll.SetHomeSpeed_Ex(0, 3, 100, speed, 200, 100, 200)
            retnZ=self.WObjdll.HomeProcess_Ex(0, 3)
        
        if not re_list[0]:
            retnX=-1
            retnX=self.WObjdll.SetHomeMode_Ex(0, 1, 0, 0, 0, -1, 2000, 400, 100)
            retnX=self.WObjdll.SetHomeSpeed_Ex(0, 1, 100, speed, 200, 100, 200)
            retnX=self.WObjdll.HomeProcess_Ex(0, 1)
            
        if not re_list[1]:
            retnY=-1
            retnY=self.WObjdll.SetHomeMode_Ex(0, 2, 0, 0, 0, -1, 2000, 400, 100)
            retnY=self.WObjdll.SetHomeSpeed_Ex(0, 2, 100, speed, 200, 100, 200)
            retnY=self.WObjdll.HomeProcess_Ex(0, 2)
            

#        
#        if retnX<0 and retnX>20:
#            print "Return Zero Fail!"
        x_Status=re_list[0]
        y_Status=re_list[1]
        z_Status=re_list[2]

        while True:
            time.sleep(1)
            if not re_list[2]:
                retnZ=self.WObjdll.GetHomeStatus_Ex(0, 3)
                zFlag=True
                if retnZ<0 or retnZ>10:
                    zFlag=False
                    z_Status=True

                    print "Z %s Return Zero Fail" %retnZ
                if retnZ==0:
                    zFlag=True
                    z_Status=True

                    print "Z %s Return Zero sucess" %retnZ
            
            #print retnX
            if not re_list[0]:
                retnX=self.WObjdll.GetHomeStatus_Ex(0, 1)
                xFlag=True
                if retnX<0 or retnX>10:
                    xFlag=False
                    x_Status=True
                    print "X %s Return Zero Fail" %retnX
                if retnX==0:
                    xFlag=True
                    x_Status=True

                    print "X %s Return Zero sucess" %retnX
            if not re_list[1]:
                retnY=self.WObjdll.GetHomeStatus_Ex(0, 2)
                yFlag=True
                if retnY<0 or retnY>10:
                    yFlag=False
                    y_Status=True

                    print "Y %s Return Zero Fail" %retnY
                if retnY==0:
                    yFlag=True
                    y_Status=True

                    print "Y %s Return Zero sucess" %retnY



#            if re_list[0] and (retnX<0 or retnX>10 or retnX==0):


            if x_Status and y_Status and z_Status:
                #return -1
                break
        return (xFlag, yFlag, zFlag)
#                
#            if retnX==0 and retnY==0 and retnZ==0:
#                break
#        return 
                
                
                #break
    def Stop(self):
        pass
        
        retnX=self.WObjdll.sudden_stop(0, 1)
        retnY=self.WObjdll.sudden_stop(0, 2)
        retnZ=self.WObjdll.sudden_stop(0, 3)
        if retnX==0 and retnY==0 and retnZ==0:
            print "stop sucess"
        
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
    c8940a1.InitCard()
    re_list=[]
    status=(False, False, False)
    re_list=  c8940a1.ReturnZero(1000, status)
    if re_list.count(True)<3:
        re_list=c8940a1.ReturnZero(500, re_list)
        if re_list.count(True)<3:
            re_list=c8940a1.ReturnZero(300, re_list)
    print re_list
    
    #c8940a1.Stop()

#cardno = CObjdll.adt8940a1_initial()
#print cardno
#dll = CDLL("8940A1.dll")
