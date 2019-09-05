# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt4.QtCore import pyqtSignature, QThread, pyqtSignal
from PyQt4.QtGui import QWidget, QMessageBox, QTextBrowser
from PyQt4 import QtCore, QtGui
import time
import random
#import xlrd,xlwt,xlutils
from html2pdf import *
from C8940A1 import *


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

        #self.timer_tv = QTextBrowser(self)

        self.btn_Next.setText("Start")
#        #self.connect(self.thread, QtCore.SIGNAL("updateDisplay"), self.updateDisplay)
#        self.timer = QtCore.QTimer(self)
#        self.work = WorkThread(parent)

        self.timer_t = TimeThread(self)
        self.timer_t.signal_time.connect(self.update_timer_tv)
        self.comm232=Com232Thread(self)
        self.comm232.signal_com232.connect(self.update_punctual)
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
        
        
        self.tableWidget.setSpan(2, 13, 3, 1)
        self.tableWidget.setSpan(5, 13, 3, 1)
        self.tableWidget.setSpan(8, 13, 3, 1)
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
        self.tableWidget.setColumnWidth(12,130)
        self.tableWidget.setColumnWidth(13,130)
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
                #self.c8940a1.Start()
                #self.timer.start(1000)
                #self.work.start()
                
        elif self.btn_Next.text()=="Stop": 
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
        time_str=time.strftime('%Y%m%d',timeArray)
        ResultDir=os.getcwd()+"\\Results\\"+str(self.mainwindow.userName)+"\\%s" %time_str
        Result=html2pdf(ResultDir, self.mainwindow.samples)
        if Result[0]:
        #self.write_excel("Results\\Excel\abc.xlsx", [["a", "b", "c"], ["aa", "bb", "cc"]])
        #reply=QMessageBox.question(self.parent,"Confirm ","Would you like to stop the test!",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            reply=QMessageBox.information(self.parent,"Information","Result file Create Success!\n%s" %Result[1],QMessageBox.Yes,QMessageBox.Yes)
        else:
            reply=QMessageBox.information(self.parent,"Information","Result file(%s) Create Failed!" %Result[1],QMessageBox.Yes,QMessageBox.Yes)

    
    #@pyqtSignature("")
    def updateDisplay(self, text):
        #get the latest date
        #move to current position
        for i in range(10):
            time.sleep(1)
            print self.parent.mainwindow.CurrentStatus
            print "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"
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
            if not sample.dr1==0.0:
              self.tableWidget.setItem(i*3+2,12 , QtGui.QTableWidgetItem(_fromUtf8(str(str("%.2f%%" %(sample.dr1*100))).encode("utf-8"))))    
            if not sample.dr2==0.0:
              self.tableWidget.setItem(i*3+3,12 , QtGui.QTableWidgetItem(_fromUtf8(str(str("%.2f%%" %(sample.dr2*100))).encode("utf-8"))))    
            if not sample.dr3==0.0:
              self.tableWidget.setItem(i*3+4,12 , QtGui.QTableWidgetItem(_fromUtf8(str(str("%.2f%%" %(sample.dr3*100))).encode("utf-8"))))    
            if not sample.dr==0.0:
              self.tableWidget.setItem(i*3+2,13 , QtGui.QTableWidgetItem(_fromUtf8(str(str("%.2f%%" %(sample.dr*100))).encode("utf-8"))))    
                                           
              
            i=i+1
        if not self.timer_t.working:
            self.btn_Next.setText("Start")
            self.btn_Privious.setEnabled(True)
            self.btn_Export.setEnabled(True)

            
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
    if self.parent.Debug:
        self.c8940a1=C8940A1()
 
  def start_timer(self):
    self.num = 0
    self.working=True

    self.start()
 
  def run(self):
    self.num = 0
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



    print "Moving to Point 1"
        #c8940a1.MoveSingleAxis(1,100000)
        #time.sleep(5)


    Axislist =[(5000,3000),(1000,0),(1000,0),(1000,0),(1000,0),(1000,0),
                   (-5000,3000),(1000,0),(1000,0),(1000,0),(1000,0),(1000,0),
                   (-5000,3000),(1000,0),(1000,0),(1000,0),(1000,0),(1000,0)]
    if self.parent.Debug:
        self.c8940a1.Set8940A1(1,1000,1000)
        self.c8940a1.Set8940A1(2,1000,1000)
        self.c8940a1.Set8940A1(3,50,50)
    x_length=0
    y_length=0
    z_length=0
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
#        print xymoved
#        if xymoved==0:
        x_length+=al[0]
        y_length+=al[1]
        if not self.working:
            break
        #print "Moving to Z"
        if self.parent.Debug:
            self.c8940a1.MoveSingleAxis(3,300,True)
        z_length+=300
        if not self.working:
            break
        #return Zero for Z
        if self.parent.Debug:
            self.c8940a1.MoveSingleAxis(3,-300,True)
#        print zmoved
#        if zmoved==0:
        z_length+=-300
        if not self.working:
            break
        self.index=self.num/6
        if self.num%6==0:
            self.parent.mainwindow.samples[self.index].op1=px
        if self.num%6==1:
            self.parent.mainwindow.samples[self.index].rp1=px
        if self.num%6==2:
            self.parent.mainwindow.samples[self.index].op2=px
        if self.num%6==3:
            self.parent.mainwindow.samples[self.index].rp2=px
        if self.num%6==4:
            self.parent.mainwindow.samples[self.index].op3=px
        if self.num%6==5:
            self.parent.mainwindow.samples[self.index].rp3=px
        
        self.parent.mainwindow.samples[self.index].calculate()
        self.signal_time.emit(px, self.num) # 发送信号
        self.sleep(1)
        if self.num==self.amount-1:
            self.working=False
        self.signal_time.emit(px, self.num) # 发送信号
        self.num += 1
        if not self.working:
            break
    #if self.working:
    if self.parent.Debug:
        self.c8940a1.MoveSingleAxis(3,-z_length,True)
        self.c8940a1.MoveMultiAxis(-x_length,-y_length,True)



  def stop(self):
    self.working=False


class Com232Thread(QThread):
  signal_com232 = pyqtSignal(float, int) # 信号
 
  def __init__(self, parent=None):
    super(Com232Thread, self).__init__(parent)
    self.working = True

  def start_com232(self):
    self.working=True
    self.start()
 
  def run(self):
      px=px-random.random()/10
      self.parent.mainwindow.samples[0].rp3=px
      #return """"


  def stop(self):
    self.working=False


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = sample_list()
    ui.show()
    sys.exit(app.exec_())
