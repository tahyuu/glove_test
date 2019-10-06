# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt4.QtCore import pyqtSignature, QThread, pyqtSignal
from PyQt4.QtGui import QWidget, QMessageBox, QTextBrowser
from PyQt4.QtGui import QWidget

from PyQt4 import QtCore, QtGui
import time
import random
#import xlrd,xlwt,xlutils
from html2pdf import *
from C8940A1 import *
import numpy as np
import pyqtgraph
import pylab
import re
import serial
import ConfigParser

g_puncual_max_value = 0.0

from Ui_sample_list import Ui_sample_list

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

from Ui_sample_list import Ui_sample_list

class sample_list(QWidget, Ui_sample_list):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None, mainwindow=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QWidget.__init__(self, parent)

        self.setupUi(self)
        self.parent=parent
        self.mainwindow=mainwindow
        self.Debug=True
        self.Comm232ReadFlag=False
        self.puncual=np.arange(1)
        self.puncual_max_value=0.0
        self.stop_pushed=False
        global g_puncual_max_value
        g_puncual_max_value = 0.0



        #######################################
        #to read config 
        #######################################
        self.cf=ConfigParser.ConfigParser()
        currentDir=os.getcwd()
        self.cf.read("%s\Config.ini" %currentDir)
        #self.cf.items("UserConfig")
        
        ######################################
        #to get debug Stutu3 in SysConfig Debug
        ######################################
        debug_status = self.cf.get('SysConfig', 'Debug_Move')
        
        self.max_puncual_limit=float(self.cf.get('XYZAxisConfig', 'max_puncual_limit'))
        self.max_pncual_limit_fine_tune=float(self.cf.get('XYZAxisConfig', 'max_pncual_limit_fine_tune'))

        if debug_status=="True":
            self.Debug=True
        else:
            self.Debug=False


        #self.timer_tv = QTextBrowser(self)

        self.btn_Next.setText("Start")
#        #self.connect(self.thread, QtCore.SIGNAL("updateDisplay"), self.updateDisplay)
#        self.timer = QtCore.QTimer(self)
#        self.work = WorkThread(parent)

        if not self.mainwindow.sample_1_enable:
            self.checkBox1.setEnabled(False)
            self.checkBox1.setChecked(False)
        if not self.mainwindow.sample_2_enable:
            self.checkBox2.setEnabled(False)
            self.checkBox2.setChecked(False)
        if not self.mainwindow.sample_3_enable:
            self.checkBox3.setEnabled(False)
            self.checkBox3.setChecked(False)

        self.checkBox1.stateChanged.connect(self.changeCheckBox)
        self.checkBox2.stateChanged.connect(self.changeCheckBox)
        self.checkBox3.stateChanged.connect(self.changeCheckBox)



        self.timer_t = TimeThread(self)
        self.timer_t.signal_time.connect(self.update_timer_tv)
        self.comm232=Com232Thread(self)
        self.comm232.signal_com232.connect(self.update_punctual)
        #self.comm232.update_graf.connect(self.UpdateGraf)
        
        self.grafthread=GrafThread(self)
        self.grafthread.update_graf.connect(self.UpdateGraf)
        self.grPlot.plotItem.showGrid(True, True, 0.7)
        self.grPlot.setYRange(0, 5)
        pen=pyqtgraph.mkPen("#FF0000",width=2)
        
#        points=100 #number of data points
#        X=np.arange(points)
#        #print np.sin(np.arange(points))
#        Y=np.sin(np.arange(points)*3*np.pi+time.time())
#        #print np.arange(points)
#        #print np.arange(points)/points*3*np.pi+time.time()
#        #Y=np.sin(np.arange(points)/points*3*np.pi+time.time())
#        #print Y
#        #C=pyqtgraph.hsvColor("130",alpha=.5)
#        pen=pyqtgraph.mkPen("#FF0000",width=2)
#        self.grPlot.plot(X,Y,pen=pen,clear=True)
        
        
        #self.timer.timeout.connect(self.work.Test)
        #self.work.trigger.connect(self.updateDisplay)
        #self.connect(self.work, QtCore.SIGNAL("updateDisplay"), self.updateDisplay)

        #set header
        self.tableWidget.setItem(0, 0, QtGui.QTableWidgetItem(_fromUtf8(str(str("Name").encode("utf-8")))))
        self.tableWidget.setItem(0, 1, QtGui.QTableWidgetItem(_fromUtf8(str(str("Color").encode("utf-8")))))
        self.tableWidget.setItem(0, 2, QtGui.QTableWidgetItem(_fromUtf8(str(str("Materia").encode("utf-8")))))
        self.tableWidget.setItem(0, 3, QtGui.QTableWidgetItem(_fromUtf8(str(str("Chemistry").encode("utf-8")))))
        self.tableWidget.setItem(0, 4, QtGui.QTableWidgetItem(_fromUtf8(str(str("Thickness").encode("utf-8")))))
        self.tableWidget.setItem(0, 5, QtGui.QTableWidgetItem(_fromUtf8(str(str("Standard").encode("utf-8")))))
        self.tableWidget.setItem(0, 6, QtGui.QTableWidgetItem(_fromUtf8(str(str("Exposed\nTime").encode("utf-8")))))
        self.tableWidget.setItem(0, 7, QtGui.QTableWidgetItem(_fromUtf8(str(str("Specimen").encode("utf-8")))))
        self.tableWidget.setItem(0, 8, QtGui.QTableWidgetItem(_fromUtf8(str(str("\t\t\t\tTest Data").encode("utf-8")))))
        self.tableWidget.setItem(1, 8, QtGui.QTableWidgetItem(_fromUtf8(str(str("Unexposed Puncture Force - OPx/N").encode("utf-8")))))
        self.tableWidget.setItem(1, 10, QtGui.QTableWidgetItem(_fromUtf8(str(str("Exposed Puncture Force - RPx/N").encode("utf-8")))))
        self.tableWidget.setItem(1, 12, QtGui.QTableWidgetItem(_fromUtf8(str(str("Degradation against chemical- DRx/%").encode("utf-8")))))
        self.tableWidget.setItem(1, 13, QtGui.QTableWidgetItem(_fromUtf8(str(str("Average Degradation - DR").encode("utf-8")))))

        self.tableWidget.setSpan(0, 0, 2, 1)
        self.tableWidget.setSpan(0, 1, 2, 1)
        self.tableWidget.setSpan(0, 2, 2, 1)
        self.tableWidget.setSpan(0, 3, 2, 1)
        self.tableWidget.setSpan(0, 4, 2, 1)
        self.tableWidget.setSpan(0, 5, 2, 1)
        self.tableWidget.setSpan(0, 6, 2, 1)
        self.tableWidget.setSpan(0, 7, 2, 1)
        self.tableWidget.setSpan(0, 8, 1, 6)
        self.tableWidget.setSpan(1, 8, 1, 2)
        self.tableWidget.setSpan(1, 10, 1, 2)

        #self.tableWidget.setSpan(0, 9, 1, 4)
        #self.tableWidget.setSpan(0, 10, 1, 4)


        self.tableWidget.setSpan(2, 0, 3, 1)
        self.tableWidget.setSpan(2, 1, 3, 1)
        self.tableWidget.setSpan(2, 2, 3, 1)
        self.tableWidget.setSpan(2, 3, 3, 1)
        self.tableWidget.setSpan(2, 4, 3, 1)
        self.tableWidget.setSpan(2, 5, 3, 1)
        self.tableWidget.setSpan(2, 6, 3, 1)
        self.tableWidget.setSpan(2, 7, 3, 1)
#
#        self.tableWidget.setSpan(0, 11, 3, 1)
# 
        self.tableWidget.setSpan(5, 0, 3, 1)
        self.tableWidget.setSpan(5, 1, 3, 1)
        self.tableWidget.setSpan(5, 2, 3, 1)
        self.tableWidget.setSpan(5, 3, 3, 1)
        self.tableWidget.setSpan(5, 4, 3, 1)
        self.tableWidget.setSpan(5, 5, 3, 1)
        self.tableWidget.setSpan(5, 6, 3, 1)
        self.tableWidget.setSpan(5, 7, 3, 1)
#
#        self.tableWidget.setSpan(3, 11, 3, 1)
# 
        self.tableWidget.setSpan(8, 0, 3, 1)
        self.tableWidget.setSpan(8, 1, 3, 1)
        self.tableWidget.setSpan(8, 2, 3, 1)
        self.tableWidget.setSpan(8, 3, 3, 1)
        self.tableWidget.setSpan(8, 4, 3, 1)
        self.tableWidget.setSpan(8, 5, 3, 1)
        self.tableWidget.setSpan(8, 6, 3, 1)
        self.tableWidget.setSpan(8, 7, 3, 1)
        
        
        self.tableWidget.setSpan(2, 12, 3, 1)
        self.tableWidget.setSpan(5, 12, 3, 1)
        self.tableWidget.setSpan(8, 12, 3, 1)
                
        self.tableWidget.setSpan(2, 13, 9, 1)
#
#        self.tableWidget.setSpan(6, 11, 3, 1)
 
 
 
#        self.tableWidget.setSpan(0, 8, 2, 1)
#        self.tableWidget.setSpan(2, 8, 2, 1)
#        self.tableWidget.setSpan(4, 8, 2, 1)



#        self.tableWidget.setSpan(0, 0, 6, 1)
#        self.tableWidget.setSpan(0, 1, 6, 1)
#        self.tableWidget.setSpan(0, 2, 6, 1)
#        self.tableWidget.setSpan(0, 3, 6, 1)
#        self.tableWidget.setSpan(0, 4, 6, 1)
#        self.tableWidget.setSpan(0, 5, 6, 1)
#        self.tableWidget.setSpan(0, 6, 6, 1)
#        self.tableWidget.setSpan(0, 7, 6, 1)
#
#        self.tableWidget.setSpan(0, 11, 6, 1)
#        
#        self.tableWidget.setSpan(0, 8, 2, 1)
#        self.tableWidget.setSpan(2, 8, 2, 1)
#        self.tableWidget.setSpan(4, 8, 2, 1)
#
#        self.tableWidget.setSpan(0, 9, 2, 1)
#        self.tableWidget.setSpan(2, 9, 2, 1)
#        self.tableWidget.setSpan(4, 9, 2, 1)
#
#        #self.tableWidget.setSpan(0, 6, 6, 1)
#
#        self.tableWidget.setSpan(6, 0, 6, 1)
#        self.tableWidget.setSpan(6, 1, 6, 1)
#        self.tableWidget.setSpan(6, 2, 6, 1)
#        self.tableWidget.setSpan(6, 3, 6, 1)
#        self.tableWidget.setSpan(6, 4, 6, 1)
#        self.tableWidget.setSpan(6, 5, 6, 1)
#        self.tableWidget.setSpan(6, 6, 6, 1)
#        self.tableWidget.setSpan(6, 7, 6, 1)
#
#        self.tableWidget.setSpan(6, 11, 6, 1)
#        
#        self.tableWidget.setSpan(6, 8, 2, 1)
#        self.tableWidget.setSpan(8, 8, 2, 1)
#        self.tableWidget.setSpan(10, 8, 2, 1)
#        
#        self.tableWidget.setSpan(6, 9, 2, 1)
#        self.tableWidget.setSpan(8, 9, 2, 1)
#        self.tableWidget.setSpan(10, 9, 2, 1)
#        
#        self.tableWidget.setSpan(12, 0, 6, 1)
#        self.tableWidget.setSpan(12, 1, 6, 1)
#        self.tableWidget.setSpan(12, 2, 6, 1)
#        self.tableWidget.setSpan(12, 3, 6, 1)
#        self.tableWidget.setSpan(12, 4, 6, 1)
#        self.tableWidget.setSpan(12, 5, 6, 1)
#        self.tableWidget.setSpan(12, 6, 6, 1)
#        self.tableWidget.setSpan(12, 7, 6, 1)
#
#        self.tableWidget.setSpan(12, 11, 6, 1)
#        
#        self.tableWidget.setSpan(12, 8, 2, 1)
#        self.tableWidget.setSpan(14, 8, 2, 1)
#        self.tableWidget.setSpan(16, 8, 2, 1)
#        
#        self.tableWidget.setSpan(12, 9, 2, 1)
#        self.tableWidget.setSpan(14, 9, 2, 1)
#        self.tableWidget.setSpan(16, 9, 2, 1)

        
#        item = self.tableWidget.item(0, 0)
#        item.setText(_translate("Dialog", "Sample1", None))
#        item = self.tableWidget.item(1, 0)
#        item.setText(_translate("Dialog", "Sample2", None))
#        item = self.tableWidget.item(2, 0)
#        item.setText(_translate("Dialog", "Sample3", None))
#        self.tableWidget.setItem(0, 0, QtGui.QTableWidgetItem(_fromUtf8(str("sample1".encode("utf-8")))))
#        self.tableWidget.setItem(6, 0, QtGui.QTableWidgetItem(_fromUtf8(str("sample2".encode("utf-8")))))
#        self.tableWidget.setItem(12, 0, QtGui.QTableWidgetItem(_fromUtf8(str("sample3".encode("utf-8")))))
#
#        self.tableWidget.setItem(0, 1, QtGui.QTableWidgetItem(_fromUtf8(str("red".encode("utf-8")))))
#        self.tableWidget.setItem(6, 1, QtGui.QTableWidgetItem(_fromUtf8(str("red".encode("utf-8")))))
#        self.tableWidget.setItem(12, 1, QtGui.QTableWidgetItem(_fromUtf8(str("red".encode("utf-8")))))
#
#        self.tableWidget.setItem(0, 2, QtGui.QTableWidgetItem(_fromUtf8(str("plastic".encode("utf-8")))))
#        self.tableWidget.setItem(6, 2, QtGui.QTableWidgetItem(_fromUtf8(str("plastic".encode("utf-8")))))
#        self.tableWidget.setItem(12, 2, QtGui.QTableWidgetItem(_fromUtf8(str("plastic".encode("utf-8")))))
#
#        self.tableWidget.setItem(0, 3, QtGui.QTableWidgetItem(_fromUtf8(str("H2SO4".encode("utf-8")))))
#        self.tableWidget.setItem(6, 3, QtGui.QTableWidgetItem(_fromUtf8(str("H2SO4".encode("utf-8")))))
#        self.tableWidget.setItem(12, 3, QtGui.QTableWidgetItem(_fromUtf8(str("H2SO4".encode("utf-8")))))
#
#        self.tableWidget.setItem(0, 4, QtGui.QTableWidgetItem(_fromUtf8(str("0.1".encode("utf-8")))))
#        self.tableWidget.setItem(6, 4, QtGui.QTableWidgetItem(_fromUtf8(str("0.1".encode("utf-8")))))
#        self.tableWidget.setItem(12, 4, QtGui.QTableWidgetItem(_fromUtf8(str("0.1".encode("utf-8")))))
#
#        self.tableWidget.setItem(0, 5, QtGui.QTableWidgetItem(_fromUtf8(str("EN374-4".encode("utf-8")))))
#        self.tableWidget.setItem(6, 5, QtGui.QTableWidgetItem(_fromUtf8(str("EN374-4".encode("utf-8")))))
#        self.tableWidget.setItem(12, 5, QtGui.QTableWidgetItem(_fromUtf8(str("EN374-4".encode("utf-8")))))       
#
#        self.tableWidget.setItem(0, 6, QtGui.QTableWidgetItem(_fromUtf8(str("Zone1".encode("utf-8")))))
#        self.tableWidget.setItem(2, 6, QtGui.QTableWidgetItem(_fromUtf8(str("Zone2".encode("utf-8")))))
#        self.tableWidget.setItem(4, 6, QtGui.QTableWidgetItem(_fromUtf8(str("Zone3".encode("utf-8")))))       
#        self.tableWidget.setItem(6, 6, QtGui.QTableWidgetItem(_fromUtf8(str("Zone1".encode("utf-8")))))
#        self.tableWidget.setItem(8, 6, QtGui.QTableWidgetItem(_fromUtf8(str("Zone2".encode("utf-8")))))
#        self.tableWidget.setItem(10, 6, QtGui.QTableWidgetItem(_fromUtf8(str("Zone3".encode("utf-8")))))       
#        self.tableWidget.setItem(12, 6, QtGui.QTableWidgetItem(_fromUtf8(str("Zone1".encode("utf-8")))))
#        self.tableWidget.setItem(14, 6, QtGui.QTableWidgetItem(_fromUtf8(str("Zone2".encode("utf-8")))))
#        self.tableWidget.setItem(16, 6, QtGui.QTableWidgetItem(_fromUtf8(str("Zone3".encode("utf-8")))))       
#
#        self.tableWidget.setItem(0, 7, QtGui.QTableWidgetItem(_fromUtf8(str("original".encode("utf-8")))))
#        self.tableWidget.setItem(1, 7, QtGui.QTableWidgetItem(_fromUtf8(str("corroded".encode("utf-8")))))
#        self.tableWidget.setItem(2, 7, QtGui.QTableWidgetItem(_fromUtf8(str("original".encode("utf-8")))))       
#        self.tableWidget.setItem(3, 7, QtGui.QTableWidgetItem(_fromUtf8(str("corroded".encode("utf-8")))))
#        self.tableWidget.setItem(4, 7, QtGui.QTableWidgetItem(_fromUtf8(str("original".encode("utf-8")))))
#        self.tableWidget.setItem(5, 7, QtGui.QTableWidgetItem(_fromUtf8(str("corroded".encode("utf-8")))))       
#        self.tableWidget.setItem(6, 7, QtGui.QTableWidgetItem(_fromUtf8(str("original".encode("utf-8")))))
#        self.tableWidget.setItem(7, 7, QtGui.QTableWidgetItem(_fromUtf8(str("corroded".encode("utf-8")))))
#        self.tableWidget.setItem(8, 7, QtGui.QTableWidgetItem(_fromUtf8(str("original".encode("utf-8")))))    
#        self.tableWidget.setItem(9, 7, QtGui.QTableWidgetItem(_fromUtf8(str("corroded".encode("utf-8")))))
#        self.tableWidget.setItem(10, 7, QtGui.QTableWidgetItem(_fromUtf8(str("original".encode("utf-8")))))
#        self.tableWidget.setItem(11, 7, QtGui.QTableWidgetItem(_fromUtf8(str("corroded".encode("utf-8")))))       
#        self.tableWidget.setItem(12, 7, QtGui.QTableWidgetItem(_fromUtf8(str("original".encode("utf-8")))))
#        self.tableWidget.setItem(13, 7, QtGui.QTableWidgetItem(_fromUtf8(str("corroded".encode("utf-8")))))
#        self.tableWidget.setItem(14, 7, QtGui.QTableWidgetItem(_fromUtf8(str("original".encode("utf-8")))))       
#        self.tableWidget.setItem(15, 7, QtGui.QTableWidgetItem(_fromUtf8(str("corroded".encode("utf-8")))))
#        self.tableWidget.setItem(16, 7, QtGui.QTableWidgetItem(_fromUtf8(str("original".encode("utf-8")))))
#        self.tableWidget.setItem(17, 7, QtGui.QTableWidgetItem(_fromUtf8(str("corroded".encode("utf-8")))))    

        stylesheet = "::section{Background-color:#A640BF;border-radius:4px;}"
        self.tableWidget.horizontalHeader().setStyleSheet(stylesheet)
        self.btn_Export.setEnabled(False)

        
        self.tableWidget.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)

        self.tableWidget.setSelectionBehavior(QtGui.QTableWidget.SelectRows)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtGui.QTableWidget.SingleSelection)
        self.tableWidget.resizeColumnsToContents()
        
        headerFont = QtGui.QFont()

        headerFont.setPointSize(14)

        headerFont.setFamily(_fromUtf8("Garamond"))

        headerFont.setBold(True)
        
        self.tableWidget.setColumnWidth(0,70)

        self.tableWidget.setColumnWidth(1,70)

        self.tableWidget.setColumnWidth(2,70)

        self.tableWidget.setColumnWidth(3,80)

        self.tableWidget.setColumnWidth(4,80)

        self.tableWidget.setColumnWidth(5,80)
        
        self.tableWidget.setColumnWidth(6,80)
        
        self.tableWidget.setColumnWidth(7,80)
        self.tableWidget.setColumnWidth(8,100)
        self.tableWidget.setColumnWidth(9,100)
        self.tableWidget.setColumnWidth(10,100)
        self.tableWidget.setColumnWidth(11,100)
        self.tableWidget.setColumnWidth(12,110)
        self.tableWidget.setColumnWidth(13,110)
        self.tableWidget.setRowHeight(1,80)
        self.tableWidget.setRowHeight(2,50)
        self.tableWidget.setRowHeight(3,50)
        self.tableWidget.setRowHeight(4,50)
        self.tableWidget.setRowHeight(5,50)
        self.tableWidget.setRowHeight(6,50)
        self.tableWidget.setRowHeight(7,50)
        self.tableWidget.setRowHeight(8,50)
        self.tableWidget.setRowHeight(9,50)
        self.tableWidget.setRowHeight(10,50)

        

        #self.tableWidget.setColumnWidth(8,100)
        #horizontalHeader()->setVisible(false);
        #self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.tableWidget.horizontalHeader().setVisible(False)
        
        for x in range(self.tableWidget.columnCount()):  
            pass

            #headItem = self.tableWidget.horizontalHeaderItem(x)  

            #headItem.setFont(headerFont)

        #headerFont.setWeight(25)
        
        #init data
        i=0
        if not self.mainwindow:
            return
        for sample in self.mainwindow.samples:
            #sample basic information
            self.tableWidget.setItem(i*3+2, 0, QtGui.QTableWidgetItem(_fromUtf8(str(str(sample.s_name).encode("utf-8")))))
            self.tableWidget.setItem(i*3+2, 1, QtGui.QTableWidgetItem(_fromUtf8(str(str(sample.s_color).encode("utf-8")))))
            self.tableWidget.setItem(i*3+2, 2, QtGui.QTableWidgetItem(_fromUtf8(str(str(sample.s_mtype).encode("utf-8")))))
            self.tableWidget.setItem(i*3+2, 3, QtGui.QTableWidgetItem(_fromUtf8(str(str(sample.s_ctype).encode("utf-8")))))
            self.tableWidget.setItem(i*3+2, 4, QtGui.QTableWidgetItem(_fromUtf8(str(str(sample.s_thickness).encode("utf-8")))))
            self.tableWidget.setItem(i*3+2, 5, QtGui.QTableWidgetItem(_fromUtf8(str(str(sample.s_standard).encode("utf-8")))))

            #sample detail information
            self.tableWidget.setItem(i*3+2, 7, QtGui.QTableWidgetItem(_fromUtf8(str(("%s" %(i+1)).encode("utf-8")))))
#            self.tableWidget.setItem(i*3+4, 7, QtGui.QTableWidgetItem(_fromUtf8(str("2".encode("utf-8")))))
#            self.tableWidget.setItem(i*3+6, 7, QtGui.QTableWidgetItem(_fromUtf8(str("3".encode("utf-8")))))   
            #self.tableWidget.setItem(0, 0, QtGui.QTableWidgetItem(_fromUtf8(str(sample.s_name.encode("utf-8")))))
#            self.tableWidget.setItem(i*3+2, 7, QtGui.QTableWidgetItem(_fromUtf8(str(("OP%s-1" %(i+1)  ).encode("utf-8")))))
#            self.tableWidget.setItem(i*3+3, 7, QtGui.QTableWidgetItem(_fromUtf8(str(("RP%s-1" %(i+1) ).encode("utf-8")))))
#            self.tableWidget.setItem(i*3+4, 7, QtGui.QTableWidgetItem(_fromUtf8(str(("OP%s-2" %(i+1)  ).encode("utf-8")))))       
#            self.tableWidget.setItem(i*3+5, 7, QtGui.QTableWidgetItem(_fromUtf8(str(("RP%s-2" %(i+1) ).encode("utf-8")))))
#            self.tableWidget.setItem(i*3+6, 7, QtGui.QTableWidgetItem(_fromUtf8(str(("OP%s-3" %(i+1) ).encode("utf-8")))))
#            self.tableWidget.setItem(i*3+7, 7, QtGui.QTableWidgetItem(_fromUtf8(str(("RP%s-3" %(i+1)  ).encode("utf-8"))))) 
            self.tableWidget.setItem(i*3+2, 8, QtGui.QTableWidgetItem(_fromUtf8(str(("OP%s-1" %(i+1) ).encode("utf-8")))))
            self.tableWidget.setItem(i*3+2, 10, QtGui.QTableWidgetItem(_fromUtf8(str(("RP%s-1" %(i+1)  ).encode("utf-8"))))) 
            self.tableWidget.setItem(i*3+3, 8, QtGui.QTableWidgetItem(_fromUtf8(str(("OP%s-2" %(i+1) ).encode("utf-8")))))
            self.tableWidget.setItem(i*3+3, 10, QtGui.QTableWidgetItem(_fromUtf8(str(("RP%s-2" %(i+1)  ).encode("utf-8"))))) 
            self.tableWidget.setItem(i*3+4, 8, QtGui.QTableWidgetItem(_fromUtf8(str(("OP%s-3" %(i+1) ).encode("utf-8")))))
            self.tableWidget.setItem(i*3+4, 10, QtGui.QTableWidgetItem(_fromUtf8(str(("RP%s-3" %(i+1)  ).encode("utf-8"))))) 
              
            i=i+1
            
            
#        item = QtGui.QTableWidgetItem()
#        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
#        self.tableWidget.setItem(0, 10, item)

    @pyqtSignature("")
    def on_btnNextStep_clicked(self):        

        #self.mainwindow.nextpushed=True

        if self.btn_Next.text()=="Start": 
            reply=QMessageBox.question(self.parent,"Confirm Information","please confirm the test sample are fixed in correct test slot!",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            if reply==QtGui.QMessageBox.No:
                return
            else:
                pass
            reply=QMessageBox.question(self.parent,"Confirm Information","please double confirm the test sample are fixed in correct test slot! test will start once you push the OK button",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            if reply==QtGui.QMessageBox.No:
                return
            else:
                if self.btn_Next.text()=="Start":
                    self.puncual_max_value=0.0

                    self.btn_Next.setText("Stop")
                    self.btn_Privious.setEnabled(False)
                    self.btn_Export.setEnabled(False)

                else:
                    self.btn_Next.setText("Start")
                    self.btn_Privious.setEnabled(True)
                    self.btn_Export.setEnabled(True)

                for i in xrange(9):
                    self.tableWidget.setItem(i+2,9 , QtGui.QTableWidgetItem(_fromUtf8(str("".encode("utf-8")))))    
                    self.tableWidget.setItem(i+2,11 , QtGui.QTableWidgetItem(_fromUtf8(str("".encode("utf-8")))))    
                    self.tableWidget.setItem(i+2,12 , QtGui.QTableWidgetItem(_fromUtf8(str("".encode("utf-8")))))    
                    self.tableWidget.setItem(i+2,13 , QtGui.QTableWidgetItem(_fromUtf8(str("".encode("utf-8")))))    

                #clean the data in samples
                for sample in self.mainwindow.samples:
                    sample.clean()
                amount=0
                if self.mainwindow.sample_1_enable:
                    amount=amount+6
                if self.mainwindow.sample_2_enable:
                    amount=amount+6
                if self.mainwindow.sample_3_enable:
                    amount=amount+6
                self.timer_t.amount=amount
                self.timer_t.start_timer()
                self.comm232.start_com232()
                self.grafthread.start_Graf_show()

                #self.c8940a1.Start()
                #self.timer.start(1000)
                #self.work.start()
                
        elif self.btn_Next.text()=="Stop": 
            self.stop_pushed=True
            reply=QMessageBox.question(self.parent,"Confirm Information","Would you like to stop the test!",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            if reply==QtGui.QMessageBox.No:
                return
            else:
                pass
                if self.btn_Next.text()=="Start":
                    self.btn_Next.setText("Stop")
                    self.btn_Privious.setEnabled(False)
                    self.btn_Export.setEnabled(False)

                else:
                    self.btn_Next.setText("Start")
                    self.btn_Privious.setEnabled(True)
                    self.btn_Export.setEnabled(True)
                self.timer_t.stop()
                #self.timer.stop()
                #self.timer_t.stop()
                #self.timer.stop()
        #self.parent.close()
        #self.mainwindow.CurrentStatus="exit"
    @pyqtSignature("")
    def on_btnPrivStep_clicked(self): 
        self.mainwindow.nextpushed=True       
        self.parent.close()
        self.mainwindow.CurrentStatus="inputInformation"
        
    @pyqtSignature("")
    def on_btnExport_clicked(self): 
        data = time.time()
        timeArray = time.localtime(data)
        time_str=time.strftime('%Y%m%d%H%M%S',timeArray)
        ResultDir=os.getcwd()+"\\Results\\"+str(self.mainwindow.userName)+"\\%s" %time_str
        file_name="%s" %(time_str)

        # to create the png for pdf.
        i=0
        all_data=[]
        for sample in self.mainwindow.samples:
            data=[]

            i=i+1
            print "1 len is %s" %len(sample.op1_list)
            print "2 len is %s" %len(sample.rp1_list)
            print "3 len is %s" %len(sample.op2_list)
            print "4 len is %s" %len(sample.rp2_list)
            print "5 len is %s" %len(sample.op3_list)
            print "6 len is %s" %len(sample.rp3_list)
            max_leng=max([len(sample.op1_list), len(sample.rp1_list), len(sample.op2_list), len(sample.rp2_list), len(sample.op3_list), len(sample.rp3_list)])
            print "max length is %s" %max_leng

            sample.op1_list=np.append(np.zeros(max_leng-len(sample.op1_list)), sample.op1_list)
            sample.rp1_list=np.append(np.zeros(max_leng-len(sample.rp1_list)), sample.rp1_list)
            sample.op2_list=np.append(np.zeros(max_leng-len(sample.op2_list)), sample.op2_list)
            print "rp2 leng is %s, max leng is %s" %(len(sample.rp2_list), max_leng)
            sample.rp2_list=np.append(np.zeros(max_leng-len(sample.rp2_list)), sample.rp2_list)
            sample.op3_list=np.append(np.zeros(max_leng-len(sample.op3_list)), sample.op3_list)
            sample.rp3_list=np.append(np.zeros(max_leng-len(sample.rp3_list)), sample.rp3_list)

            #sample.rp3_list=sample.rp3_list[0:max_leng-1]
            print "1 len is %s" %len(sample.op1_list)
            print "2 len is %s" %len(sample.rp1_list)
            print "3 len is %s" %len(sample.op2_list)
            print "4 len is %s" %len(sample.rp1_list)
            print "5 len is %s" %len(sample.op3_list)
            print "6 len is %s" %len(sample.rp3_list)
            data.append(sample.op1_list)
            data.append(sample.rp1_list)
            data.append(sample.op2_list)
            data.append(sample.rp2_list)
            data.append(sample.op3_list)
            data.append(sample.rp3_list)
            #print data
            file_root=os.path.join(ResultDir, file_name)
            print "file root is %s, and %s" %(file_name,i)
            sample.s_firgure_img=("%s-%s.png" %(file_root, i))

            CharCreate(data, "%s-%s" %(file_root, i))
            all_data.extend(data)
        Result=WriteExcel(all_data, file_root)
        
        Result=html2pdf(ResultDir, self.mainwindow.samples)
        

        if Result[0]:
        #self.write_excel("Results\\Excel\abc.xlsx", [["a", "b", "c"], ["aa", "bb", "cc"]])
        #reply=QMessageBox.question(self.parent,"Confirm ","Would you like to stop the test!",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            reply=QMessageBox.information(self.parent,"Information","Result file Create Success!\n%s" %Result[1],QMessageBox.Yes,QMessageBox.Yes)
        else:
            reply=QMessageBox.information(self.parent,"Information","Result file(%s) Create Failed!" %Result[1],QMessageBox.Yes,QMessageBox.Yes)

    def UpdateGraf(self):
        #        points=100 #number of data points
        #print self.puncual
        tmp_punctual = self.puncual.copy()
        X=np.arange(len(tmp_punctual))
        #print len(tmp_punctual)
        #print np.sin(np.arange(points))
        #Y=np.sin(np.arange(points)*3*np.pi+time.time())
        Y=tmp_punctual
        #print np.arange(points)
        #print np.arange(points)/points*3*np.pi+time.time()
        #Y=np.sin(np.arange(points)/points*3*np.pi+time.time())
        #print Y
        #C=pyqtgraph.hsvColor("130",alpha=.5)
        pen=pyqtgraph.mkPen("#FF0000",width=2)
        #self.grPlot.setXRange(0, 60)
        self.grPlot.plot(X,Y,pen=pen,clear=True)


    def changeCheckBox(self):
        i=0
        dr=0
        dr_sum=0.0
        dr_count=0
        for sample in self.mainwindow.samples:
            if i==0 and self.checkBox1.isChecked():
                dr_sum=sample.dr+dr_sum
                dr_count=dr_count+1
            if i==1 and self.checkBox2.isChecked():
                dr_sum=sample.dr+dr_sum
                dr_count=dr_count+1

            if i==2 and self.checkBox3.isChecked():
                dr_sum=sample.dr+dr_sum
                dr_count=dr_count+1

            i=i+1

        if dr_count!=0:
            dr=dr_sum/dr_count
            self.tableWidget.setItem(2,13 , QtGui.QTableWidgetItem(_fromUtf8(str(str("%.2f%%" %(dr*100))).encode("utf-8")))) 
            ################################
            #to calculate the avg of dr for each sample
            ################################
            i=0
            for sample in self.mainwindow.samples:  
                print dr
                if i==0:
                    if self.checkBox1.isChecked():
                        sample.dr_avg=dr
                    else:
                        sample.dr_avg=0.0
                if i==1:
                    if self.checkBox2.isChecked():
                        sample.dr_avg=dr
                    else:
                        sample.dr_avg=0.0
                if i==2:
                    if self.checkBox3.isChecked():
                        sample.dr_avg=dr
                    else:
                        sample.dr_avg=0.0
                i=i+1
        else:
            self.tableWidget.setItem(2,13 , QtGui.QTableWidgetItem(_fromUtf8(str(str("")).encode("utf-8")))) 


        
    #@pyqtSignature("")
    def updateDisplay(self, text):
        #get the latest date
        #move to current position
        for i in range(10):
            time.sleep(1)
            print self.parent.mainwindow.CurrentStatus

    def stop_at_max_puncual(self):
        self.timer_t.stop_at_max_puncual()
    def update_punctual(self, value, number):
        print "%s = %s" %(value, number)
        pass
    def update_timer_tv(self, value, number):
        i=0
        if number%2==0:
            self.tableWidget.setItem(number/2+2,9 , QtGui.QTableWidgetItem(_fromUtf8(str(str("%.3f" %value).encode("utf-8")))))   
        else:
            self.tableWidget.setItem(number/2+2,11 , QtGui.QTableWidgetItem(_fromUtf8(str(str("%.3f" %value).encode("utf-8")))))   

        for sample in self.mainwindow.samples:
#            if not sample.dr1==0.0:
#              self.tableWidget.setItem(i*3+2,12 , QtGui.QTableWidgetItem(_fromUtf8(str(str("%.2f%%" %(sample.dr1*100))).encode("utf-8"))))    
#            if not sample.dr2==0.0:
#              self.tableWidget.setItem(i*3+3,12 , QtGui.QTableWidgetItem(_fromUtf8(str(str("%.2f%%" %(sample.dr2*100))).encode("utf-8"))))    
#            if not sample.dr3==0.0:
#              self.tableWidget.setItem(i*3+4,12 , QtGui.QTableWidgetItem(_fromUtf8(str(str("%.2f%%" %(sample.dr3*100))).encode("utf-8"))))    
            if not sample.dr==0.0:
              self.tableWidget.setItem(i*3+2,12 , QtGui.QTableWidgetItem(_fromUtf8(str(str("%.2f%%" %(sample.dr*100))).encode("utf-8"))))    
                                           
            i=i+1
        if not self.timer_t.working:
            self.btn_Next.setText("Start")
            self.btn_Privious.setEnabled(True)
            self.btn_Export.setEnabled(True)
            self.comm232.stop()

            
    def write_excel(self, filename, data):
        book = xlwt.Workbook()            #创建excel对象
        sheet = book.add_sheet('sheet1')  #添加一个表
        c = 0  #保存当前列
        for d in data: #取出data中的每一个元组存到表格的每一行
            for index in range(len(d)):   #将每一个元组中的每一个单元存到每一列
                sheet.write(c,index,d[index])
            c += 1
        book.save(filename) #保存excel
        #self.timer_tv.setText(self.tr(text + " " + str(number)))
#    def closeEvent(self,event):
#
#        reply = QtGui.QMessageBox.question(self,'Message',"Are you sure to quit?", QtGui.QMessageBox.Yes|QtGui.QMessageBox.No, QtGui.QMessageBox.No)
#
#        if reply == QtGui.QMessageBox.Yes:
#            event.accept()
#        else:
#            event.ignore()

class TimeThread(QThread):
  signal_time = pyqtSignal(float, int) # 信号
 
  def __init__(self, parent=None):
    super(TimeThread, self).__init__(parent)
    self.working = True
    self.amount=0
    self.num = 0
    self.parent=parent
    self.x_start_point=int(self.parent.cf.get('XYZAxisConfig', 'x_start_point'))
    self.y_start_point=int(self.parent.cf.get('XYZAxisConfig', 'y_start_point'))
    self.z_start_point=int(self.parent.cf.get('XYZAxisConfig', 'z_start_point'))
    self.punctual_route=int(self.parent.cf.get('XYZAxisConfig', 'max_puncual_route'))
    self.x_interval=int(self.parent.cf.get('XYZAxisConfig', 'x_interval'))
    self.y_interval=int(self.parent.cf.get('XYZAxisConfig', 'y_interval'))
    self.x_speed=int(self.parent.cf.get('XYZAxisConfig', 'x_speed'))
    self.y_speed=int(self.parent.cf.get('XYZAxisConfig', 'y_speed'))
    self.z_speed_1=int(self.parent.cf.get('XYZAxisConfig', 'z_speed_1'))
    self.z_speed_2=int(self.parent.cf.get('XYZAxisConfig', 'z_speed_2'))

#    self.x_start_point=43069
#    self.y_start_point=31406
#    self.z_start_point=97979
#    #self.z_start_point=127979
#
#    self.punctual_route=10000
#    self.x_interval=40000
#    self.y_interval=50000
#    self.x_speed=20000
#    self.y_speed=10000
#    self.z_speed_1=30000
#    self.z_speed_2=5000
    
    if self.parent.Debug:
        self.c8940a1=C8940A1()
 
  def start_timer(self):
    self.num = 0
    self.working=True

    self.start()
 
  def run(self):
    self.num = 0
    self.x_length=0
    self.y_length=0
    self.z_length=0
    px=1
#    while self.working and self.num<self.amount:
#
#        print "Working", self.thread()
#        print "self number is: %s" %(self.num)
#        self.index=self.num/6
#        print "self index is: %s" %(self.index)
#        print len(self.parent.mainwindow.samples)
#        #      if self.num%6==0:
#        self.parent.mainwindow.samples[self.index].op1=px
#      if self.num%6==1:
#        self.parent.mainwindow.samples[self.index].rp1=px
#      if self.num%6==2:
#        self.parent.mainwindow.samples[self.index].op2=px
#      if self.num%6==3:
#        self.parent.mainwindow.samples[self.index].rp2=px
#      if self.num%6==4:
#        self.parent.mainwindow.samples[self.index].op3=px
#      if self.num%6==5:
#        self.parent.mainwindow.samples[self.index].rp3=px



    print "coding return zero here!"
        #c8940a1.MoveSingleAxis(1,100000)
        #time.sleep(5)
    


    
    Axislist =[(self.x_start_point,self.y_start_point),(self.x_interval,0),(self.x_interval,0),(self.x_interval,0),(self.x_interval,0),(self.x_interval,0),
                   (-(self.x_interval*5),self.y_interval),(self.x_interval,0),(self.x_interval,0),(self.x_interval,0),(self.x_interval,0),(self.x_interval,0),
                   (-(self.x_interval*5),self.y_interval),(self.x_interval,0),(self.x_interval,0),(self.x_interval,0),(self.x_interval,0),(self.x_interval,0)]
    if self.parent.Debug:
        #return zero
        #######################################
        #quickly reutrun to zero for XYZ
        #######################################
        command_position_x=self.c8940a1.Get_command_pos(1)
        command_position_y=self.c8940a1.Get_command_pos(2)
        command_position_z=self.c8940a1.Get_command_pos(3)
        self.c8940a1.Set8940A1(1,1000,self.x_speed)
        self.c8940a1.Set8940A1(2,1000,self.y_speed)
        self.c8940a1.Set8940A1(3,1000,self.z_speed_1)       
        
        if command_position_z>0:
            self.c8940a1.MoveSingleAxis(3,-command_position_z,True)
        if command_position_x>0 and command_position_y:
            self.c8940a1.MoveMultiAxis(-command_position_x,-command_position_y)
        command_position_y=self.c8940a1.Get_command_pos(2)
        if command_position_y>0:
            self.c8940a1.MoveSingleAxis(2,-command_position_y,True)

        #######################################
        #below code is for Z return zero
        #######################################
        re_list=[]
        status=(True, True, False)
        re_list=  self.c8940a1.ReturnZero(2000, status)
        while re_list.count(True)<3:
            re_list=self.c8940a1.ReturnZero(1000, re_list)
            if re_list.count(True)<3:
                self.c8940a1.ReturnZero(500, re_list)
                if re_list.count(True)<3:
                    self.c8940a1.ReturnZero(300, re_list)
        #######################################

        #######################################
        #below code is for XY return zero
        #######################################
        re_list=[]
        status=(False, False, False)
        re_list=  self.c8940a1.ReturnZero(1000, status)
        while re_list.count(True)<3:
            re_list=self.c8940a1.ReturnZero(500, re_list)
            if re_list.count(True)<3:
                self.c8940a1.ReturnZero(300, re_list)
        #######################################
        #below code will set the speed of each axis
        #######################################
        self.c8940a1.Set8940A1(1,1000,self.x_speed)
        self.c8940a1.Set8940A1(2,1000,self.y_speed)
        self.c8940a1.Set8940A1(3,1000,self.z_speed_1)
    self.x_length=0
    self.y_length=0
    self.z_length=0
    i=0
    for al in Axislist:
        if self.num%6==0:
            px=1
        px=px-random.random()/10
        


        #c8940a1.MoveSingleAxis(2,100000)
        #print "Moving to XY"
        if not self.working:
            break
        if self.parent.Debug:
            self.c8940a1.MoveMultiAxis(al[0],al[1])
        else:
            self.parent.comm232.global_index=0
#        print xymoved
#        if xymoved==0:
        self.x_length+=al[0]
        self.y_length+=al[1]
        if not self.working:
            break
        #print "Moving to Z"
        if self.parent.Debug:
            ######################################
            #Z Axis to find Zero here      --------------------------------------------no need to find zero for every test
            ######################################
#            status=(True, True, False)
#            re_list=  self.c8940a1.ReturnZero(1000, status)
#            if re_list.count(True)<3:
#                re_list=self.c8940a1.ReturnZero(500, re_list)
#                if re_list.count(True)<3:
#                    re_list=self.c8940a1.ReturnZero(300, re_list)
            #print re_list
            #self.c8940a1.MoveSingleAxis(3,self.z_start_point,True)
            ######################################
            #move Z axis to z start point at z_speed_1
            ######################################
            if not self.working:
                break
            if i==0:
                self.c8940a1.Set8940A1(3,1000,self.z_speed_1)
                self.c8940a1.MoveSingleAxis(3,self.z_start_point,True)
            ######################################
            #Start to get the punctual at z_speed_2, max route is punctual_route.
            ######################################
            print "self.punctual_route is %s" %self.punctual_route
            ######################################
            #Set puncual puncual_max_value to Zero.
            ######################################
            self.parent.Comm232ReadFlag=False

            while True:
                self.parent.puncual=np.arange(1)
                if len(self.parent.puncual)==1:
                    break
            #set puncual_max_value to zero
            global g_puncual_max_value
            while True:
                g_puncual_max_value=0.0
                if  g_puncual_max_value==0.0:
                    break
            while True:
                self.parent.puncual_max_value=0.0
                if  self.parent.puncual_max_value==0.0:
                    break
            if not self.working:
                break    
            self.parent.Comm232ReadFlag=True
            self.c8940a1.Set8940A1(3,1000,self.z_speed_2)
            self.c8940a1.MoveSingleAxis(3,self.punctual_route,True)
            ######################################
            #reset back to z_speed_1 after finished the punctual getting.
            ######################################
            self.c8940a1.Set8940A1(3,1000,self.z_speed_1)
            time.sleep(0.5)
            self.parent.Comm232ReadFlag=False
        else:
            self.parent.puncual=np.arange(1)
            self.parent.Comm232ReadFlag=True
            time.sleep(1)
            self.parent.Comm232ReadFlag=False
        self.z_length+=(self.z_start_point+self.punctual_route)
        if not self.working:
            break
        #return Zero for Z
        if self.parent.Debug:
            #####################################
            #after finised the test, return Z Axis need return to Zero
            # 1, rough move to Zero
            # 2, no need return Zero because we have return Zero at the beggin of test
            #####################################
            command_position=self.c8940a1.Get_command_pos(3)
            print "A is %s; B is %s"%(command_position-self.z_start_point,  -(self.z_start_point+self.punctual_route))
            #self.c8940a1.MoveSingleAxis(3,-(self.z_start_point+self.punctual_route),True)
            if command_position>self.z_start_point:
                self.c8940a1.MoveSingleAxis(3,-(command_position-self.z_start_point),True)
#        print zmoved
#        if zmoved==0:
        self.z_length+=-(self.z_start_point+self.punctual_route)
        print "self working is %s" %self.working
        if not self.working:
            break
        #####################################
        #if parent Debug is False then excute with debug model
        #####################################
        ###########################################
        #Saving the puncual value to mainwindow so that we can store them
        ###########################################
        time.sleep(1)
        if self.parent.Debug:
            self.index=self.num/6
            if self.num%6==0:
                self.parent.mainwindow.samples[self.index].op1=self.parent.puncual_max_value
                print "puncual value is"
                print self.parent.puncual
                print "before value is "
                print self.parent.mainwindow.samples[self.index].op1_list
                self.parent.mainwindow.samples[self.index].op1_list=self.parent.puncual.copy()
                print "after value is "
                print self.parent.mainwindow.samples[self.index].op1_list
            if self.num%6==1:
                self.parent.mainwindow.samples[self.index].rp1=self.parent.puncual_max_value
                self.parent.mainwindow.samples[self.index].rp1_list=self.parent.puncual.copy()   
            if self.num%6==2:
                self.parent.mainwindow.samples[self.index].op2=self.parent.puncual_max_value
                self.parent.mainwindow.samples[self.index].op2_list=self.parent.puncual.copy()
            if self.num%6==3:
                self.parent.mainwindow.samples[self.index].rp2=self.parent.puncual_max_value
                self.parent.mainwindow.samples[self.index].rp2_list=self.parent.puncual.copy()
            if self.num%6==4:
                self.parent.mainwindow.samples[self.index].op3=self.parent.puncual_max_value
                self.parent.mainwindow.samples[self.index].op3_list=self.parent.puncual.copy()
            if self.num%6==5:
                self.parent.mainwindow.samples[self.index].rp3=self.parent.puncual_max_value
                self.parent.mainwindow.samples[self.index].rp3_list=self.parent.puncual.copy()

        else:
            self.index=self.num/6
            if self.num%6==0:
                self.parent.mainwindow.samples[self.index].op1=px
                print "puncual value is"
                print self.parent.puncual
                print "before value is "
                print self.parent.mainwindow.samples[self.index].op1_list
                self.parent.mainwindow.samples[self.index].op1_list=self.parent.puncual.copy()
                print "after value is "
                print self.parent.mainwindow.samples[self.index].op1_list
            if self.num%6==1:
                self.parent.mainwindow.samples[self.index].rp1=px
                self.parent.mainwindow.samples[self.index].rp1_list=self.parent.puncual.copy()   

            if self.num%6==2:
                self.parent.mainwindow.samples[self.index].op2=px
                self.parent.mainwindow.samples[self.index].op2_list=self.parent.puncual.copy()

            if self.num%6==3:
                self.parent.mainwindow.samples[self.index].rp2=px
                self.parent.mainwindow.samples[self.index].rp2_list=self.parent.puncual.copy()

            if self.num%6==4:
                self.parent.mainwindow.samples[self.index].op3=px
                self.parent.mainwindow.samples[self.index].op3_list=self.parent.puncual.copy()

            if self.num%6==5:
                self.parent.mainwindow.samples[self.index].rp3=px
                self.parent.mainwindow.samples[self.index].rp3_list=self.parent.puncual.copy()

            
        self.parent.mainwindow.samples[self.index].calculate()
        self.signal_time.emit(self.parent.puncual_max_value, self.num) # 发送信号
        self.sleep(1)
        if self.num==self.amount-1:
            self.working=False
        self.signal_time.emit(self.parent.puncual_max_value, self.num) # 发送信号
        self.num += 1
        if not self.working:
            break
        i=i+1
    # to show dr after teste finished
    self.parent.changeCheckBox()
    #if self.working:
    ###########################################
    #return to zero after finish test
    ###########################################
    if self.parent.Debug:
        command_position_x=self.c8940a1.Get_command_pos(1)
        command_position_y=self.c8940a1.Get_command_pos(2)
        command_position_z=self.c8940a1.Get_command_pos(3)
        if command_position_z>0:
            self.c8940a1.MoveSingleAxis(3,-command_position_z,True)
        #######################################
        #below code is for Z return zero
        #######################################
        re_list=[]
        status=(True, True, False)
        re_list=  self.c8940a1.ReturnZero(10000, status)

        while re_list.count(True)<3:
#            command_position_z=self.c8940a1.Get_command_pos(3)
#            self.c8940a1.MoveSingleAxis(3,-command_position_z,True)
            re_list=  self.c8940a1.ReturnZero(2000, status)
            if  re_list.count(True)<3:
                re_list=self.c8940a1.ReturnZero(1000, re_list)
                if re_list.count(True)<3:
                    self.c8940a1.ReturnZero(500, re_list)
                    if re_list.count(True)<3:
                        self.c8940a1.ReturnZero(300, re_list)
        #######################################
        self.c8940a1.MoveMultiAxis(-self.x_length,-self.y_length,True)
#        self.c8940a1.MoveSingleAxis(3,-z_length,True)
#        self.c8940a1.MoveMultiAxis(-x_length,-y_length,True)

  def stop_at_max_puncual(self):
        self.c8940a1.Stop()
        command_position=self.c8940a1.Get_command_pos(3)
        if command_position>self.z_start_point:
            print "return position is %s " %-(command_position-self.z_start_point)
            self.c8940a1.MoveSingleAxis(3,-(command_position-self.z_start_point),True)
        ###########################
        #set to zero
        # why need set puncual  and puncual_max_value here? Can we skip it.
        # there is some bugs here, need to be fixed
        #试一下将self.parent.puncual清空的动作去掉，只留g_puncual_max_value 赋值的动作----perfect
        ###########################
#        while True:
#            self.parent.puncual=np.arange(1)
#            if len(self.parent.puncual)==1:
#                break
        #set puncual_max_value to zero
        global g_puncual_max_value
        while True:
            g_puncual_max_value=0.0
            if  g_puncual_max_value==0.0:
                break
#        while True:
#            self.parent.puncual_max_value=0.0
#            if  self.parent.puncual_max_value==0.0:
#                break

  def stop(self):
      
    #Z axis return Zero
    self.working=False
    if self.parent.Debug:
        if self.parent.stop_pushed:
            self.c8940a1.Stop()
            pass
            #######################################
            #quickly reutrun to zero for XYZ
            #######################################
#            command_position_x=self.c8940a1.Get_command_pos(1)
#            command_position_y=self.c8940a1.Get_command_pos(2)
#            command_position_z=self.c8940a1.Get_command_pos(3)
#            print "command position -z is %s" %-command_position_z
##            self.c8940a1.Set8940A1(1,1000,self.x_speed)
##            self.c8940a1.Set8940A1(2,1000,self.y_speed)
#            self.c8940a1.Set8940A1(3,1000,self.z_speed_1)       
#            
#            self.c8940a1.MoveSingleAxis(3,-command_position_z,True)
#            self.c8940a1.MoveMultiAxis(-command_position_x,-command_position_y)
#            command_position_y=self.c8940a1.Get_command_pos(2)
#            self.c8940a1.MoveSingleAxis(2,-command_position_y,True)
#        if self.z_length>0:
#            self.c8940a1.MoveSingleAxis(3,-(self.z_length),True)
#        if self.x_length>0 and self.y_length>0:
#            self.c8940a1.MoveMultiAxis(-self.x_length,-self.y_length,True)



def dev(i):
    return i/100
def mean(a):
    return sum(a) / len(a)
    
class Com232Thread(QThread):
  signal_com232 = pyqtSignal(float, int) # 信号
  #update_graf = pyqtSignal() # 信号

  def __init__(self, parent=None):
    super(Com232Thread, self).__init__(parent)
    self.working = True
    self.parent=parent
    self.global_index=1


  def start_com232(self):

    self.punctual=[]
    self.working=True

    self.start()

 
  def run(self):
    #print self.parent.Comm232ReadFlag

    r_pun_data = r'\d(?P<data>[\+|-]\d{5})'
    pattern = re.compile(r_pun_data)
    self.serial_obj = serial.Serial('COM1', 9600)
    if self.serial_obj.isOpen():
       print("open success")
    else:
        print("open failed")
    avg = -0.001
    if True:
        old_data=""
        while  self.working:
            count =0
#            try:
#                count = self.serial_obj.inWaiting()
#            except:
#                pass
            if self.parent.Debug:
                time.sleep(0.02)
                count = self.serial_obj.inWaiting()
                if count > 8:
                    
                    #print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX%s" %self.parent.Comm232ReadFlag
                    data = old_data + self.serial_obj.read(count)
                    #print "data is %s" %data
                    if not old_data:
                        pass
                        #print "old data  + new data is XXXXXXXXXXXXXXXXXXXXXXXX %s" %old_data

                    #old_data=""
                    #####################################
                    #change the readflag after read, maybe it will solove the problem when the puncual get max value, the next one didn't test
                    #####################################
                    if not self.parent.Comm232ReadFlag:
                        pass
                        #continue
                    #if
                    #print data
                    data_arry=pattern.findall(data)

                    
                    tmp_array=map(float,data_arry)
                    tmp_array=map(dev,tmp_array)

                    if not tmp_array:
                        #old_data=data
                        continue
                        
                    ##############################
                    #找到最后匹配的字符串的位置
                    ###############################
#                    if data[::-1].find(data_arry[-1][::-1])>0:
#                        print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
#                    print data[::-1].find(data_arry[-1][::-1])
                    old_data=data[len(data)-data[::-1].find(data_arry[-1][::-1]):]
                    #print data_arry[-1]
                    
                    #print "odl data is XXXXXXXXXXXXXXXXXXXXXXXX %s" %old_data

                    ####################################################
                    #if the serial port always report the same value, then not save them
                    ####################################################
                    if tmp_array.count(tmp_array[-1])==len(tmp_array):
                        #old_data=data
                        continue

                    if len(tmp_array)==1 and  abs(abs(tmp_array[0])-abs(avg))/(abs(avg)+0.0001)>0.8:
                        #old_data=data
                        continue

                    #########################################
                    #to choose the correct value for punctual 
                    #########################################                    
    #                if len(tmp_array)>0:
                    if len(tmp_array)>1 and abs(abs(tmp_array[0])-abs(tmp_array[1]))/(abs(tmp_array[1])+0.0001)>0.8:
                        tmp_array.pop(1)
                    if len(tmp_array)>1 and abs(abs(tmp_array[-2])-abs(tmp_array[-1]))/(abs(tmp_array[-2])+0.0001)>0.8:
                        tmp_array.pop(-1)
                    if len(tmp_array)>0:
                        avg = sum(tmp_array) / len(tmp_array)
                else:
                    continue
            else:
                ########################################################
                #below line for debug data create
                ########################################################
                tmp_array=[]
                for i in xrange(10):
                    time.sleep(0.01)
                    tmp_array.append(0.005*self.global_index*self.global_index)
                    self.global_index=self.global_index+1

                    #tmp_array=np.random.rand(10)
                #print tmp_array
            ##############################################
            #here should be 前进一格tab(Done)
            ##############################################
            #print tmp_array
            if  self.parent.Comm232ReadFlag:
                self.parent.puncual=np.append(self.parent.puncual, tmp_array)
                #print self.parent.puncual
                #########################################
                #to set max puncual value
                #########################################
            if len(tmp_array)>0:
                global g_puncual_max_value
                g_puncual_max_value = (g_puncual_max_value>=max(tmp_array)) and g_puncual_max_value or max(tmp_array)
                self.parent.puncual_max_value =(self.parent.puncual_max_value>=max(tmp_array)) and self.parent.puncual_max_value or max(tmp_array)

                #########################################
                #stop C8940A1 if get max_puncual_limit during test
                #########################################
                #print "current value is%s  max limit is %s" %(g_puncual_max_value, self.parent.max_puncual_limit)
#                if self.parent.Debug and self.parent.puncual_max_value>=self.parent.max_puncual_limit:
#                    self.parent.stop_at_max_puncual()
#                    self.parent.Comm232ReadFlag=False
            
            ##############################################
            #here should be 前进一格tab(Done)
            #bug hrere 当压力达到最大值时，将parent.puncual 赋值为空，导致无法当前测试数据
            ##############################################
            if self.parent.Debug and g_puncual_max_value>=self.parent.max_puncual_limit*self.parent.max_pncual_limit_fine_tune:
                self.parent.stop_at_max_puncual()
                self.parent.Comm232ReadFlag=False

            #print self.parent.puncual
                    #self.working
                    #break
                    
                #print self.parent.puncual
                #print "OK"
#                if data != b'':
#                    print("receive:", data)
#                    serial.write(data)
#                else:
#                    serial.write(hexsend(data))
    if self.parent.Debug:
        self.serial_obj.close()
    try:
        pass

    except KeyboardInterrupt:
        if self.serial_obj != None:
            self.serial_obj.close()

  def stop(self):
    self.working=False 
    time.sleep(0.1)
    if self.serial_obj != None:
        self.serial_obj.close()


class GrafThread(QThread):
  update_graf = pyqtSignal() # 信号

  def __init__(self, parent=None):
    super(GrafThread, self).__init__(parent)
    self.working = True
    self.parent=parent

  def start_Graf_show(self):
    self.working=True
    self.start()
 
  def run(self):
    #print self.parent.Comm232ReadFlag
    while True:
        #print self.parent.Comm232ReadFlag
        #print  self.parent.puncual
        #px=2
        if self.parent.Comm232ReadFlag:
            time.sleep(0.1)
            #px=px-random.random()/10
            #self.punctual.append(px)
            #self.parent.puncual=np.append(self.parent.puncual, px)
            self.update_graf.emit() # 发送信号

            #print  self.parent.puncual
        else:
            pass
            #print self.parent.Comm232ReadFlag


  def stop(self):
    self.working=False


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = sample_list()
    ui.show()
    sys.exit(app.exec_())
