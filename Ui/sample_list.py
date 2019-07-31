# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt4.QtCore import pyqtSignature, QThread, pyqtSignal
from PyQt4.QtGui import QWidget, QMessageBox, QTextBrowser
from PyQt4 import QtCore, QtGui
import time
import random


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
        #self.timer_tv = QTextBrowser(self)

        self.btn_Next.setText("Start")
#        #self.connect(self.thread, QtCore.SIGNAL("updateDisplay"), self.updateDisplay)
#        self.timer = QtCore.QTimer(self)
#        self.work = WorkThread(parent)

        self.timer_t = TimeThread()
        self.timer_t.signal_time.connect(self.update_timer_tv)
        #self.timer_t.signal_time.connect(self.update_timer_tv)
        #self.timer.timeout.connect(self.work.Test)
        #self.work.trigger.connect(self.updateDisplay)
        #self.connect(self.work, QtCore.SIGNAL("updateDisplay"), self.updateDisplay)

        self.tableWidget.setSpan(0, 0, 6, 1)
        self.tableWidget.setSpan(0, 1, 6, 1)
        self.tableWidget.setSpan(0, 2, 6, 1)
        self.tableWidget.setSpan(0, 3, 6, 1)
        self.tableWidget.setSpan(0, 4, 6, 1)
        self.tableWidget.setSpan(0, 5, 6, 1)
        
        self.tableWidget.setSpan(0, 6, 2, 1)
        self.tableWidget.setSpan(2, 6, 2, 1)
        self.tableWidget.setSpan(4, 6, 2, 1)

        #self.tableWidget.setSpan(0, 6, 6, 1)

        self.tableWidget.setSpan(6, 0, 6, 1)
        self.tableWidget.setSpan(6, 1, 6, 1)
        self.tableWidget.setSpan(6, 2, 6, 1)
        self.tableWidget.setSpan(6, 3, 6, 1)
        self.tableWidget.setSpan(6, 4, 6, 1)
        self.tableWidget.setSpan(6, 5, 6, 1)
        
        self.tableWidget.setSpan(6, 6, 2, 1)
        self.tableWidget.setSpan(8, 6, 2, 1)
        self.tableWidget.setSpan(10, 6, 2, 1)
        
        self.tableWidget.setSpan(12, 0, 6, 1)
        self.tableWidget.setSpan(12, 1, 6, 1)
        self.tableWidget.setSpan(12, 2, 6, 1)
        self.tableWidget.setSpan(12, 3, 6, 1)
        self.tableWidget.setSpan(12, 4, 6, 1)
        self.tableWidget.setSpan(12, 5, 6, 1)
        
        self.tableWidget.setSpan(12, 6, 2, 1)
        self.tableWidget.setSpan(14, 6, 2, 1)
        self.tableWidget.setSpan(16, 6, 2, 1)
        
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

        
        self.tableWidget.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)

        self.tableWidget.setSelectionBehavior(QtGui.QTableWidget.SelectRows)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtGui.QTableWidget.SingleSelection)
        self.tableWidget.resizeColumnsToContents()
        
        headerFont = QtGui.QFont()

        headerFont.setPointSize(10)

        headerFont.setFamily(_fromUtf8("Garamond"))

        headerFont.setBold(True)
        
        self.tableWidget.setColumnWidth(0,100)

        self.tableWidget.setColumnWidth(1,80)

        self.tableWidget.setColumnWidth(2,100)

        self.tableWidget.setColumnWidth(3,100)

        self.tableWidget.setColumnWidth(4,100)

        self.tableWidget.setColumnWidth(5,100)
        
        self.tableWidget.setColumnWidth(6,100)
        
        self.tableWidget.setColumnWidth(7,100)
        #self.tableWidget.setColumnWidth(8,100)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        
        for x in range(self.tableWidget.columnCount()):  

            headItem = self.tableWidget.horizontalHeaderItem(x)  

            headItem.setFont(headerFont)

        #headerFont.setWeight(25)
        
        #init data
        i=0
        for sample in self.mainwindow.samples:
            #sample basic information
            self.tableWidget.setItem(i*6, 0, QtGui.QTableWidgetItem(_fromUtf8(str(str(sample.s_name).encode("utf-8")))))
            self.tableWidget.setItem(i*6, 1, QtGui.QTableWidgetItem(_fromUtf8(str(str(sample.s_color).encode("utf-8")))))
            self.tableWidget.setItem(i*6, 2, QtGui.QTableWidgetItem(_fromUtf8(str(str(sample.s_mtype).encode("utf-8")))))
            self.tableWidget.setItem(i*6, 3, QtGui.QTableWidgetItem(_fromUtf8(str(str(sample.s_ctype).encode("utf-8")))))
            self.tableWidget.setItem(i*6, 4, QtGui.QTableWidgetItem(_fromUtf8(str(str(sample.s_thickness).encode("utf-8")))))
            self.tableWidget.setItem(i*6, 5, QtGui.QTableWidgetItem(_fromUtf8(str(str(sample.s_standard).encode("utf-8")))))

            #sample detail information
            self.tableWidget.setItem(i*6, 6, QtGui.QTableWidgetItem(_fromUtf8(str("Zone1".encode("utf-8")))))
            self.tableWidget.setItem(i*6+2, 6, QtGui.QTableWidgetItem(_fromUtf8(str("Zone2".encode("utf-8")))))
            self.tableWidget.setItem(i*6+4, 6, QtGui.QTableWidgetItem(_fromUtf8(str("Zone3".encode("utf-8")))))   
            #self.tableWidget.setItem(0, 0, QtGui.QTableWidgetItem(_fromUtf8(str(sample.s_name.encode("utf-8")))))
            self.tableWidget.setItem(i*6, 7, QtGui.QTableWidgetItem(_fromUtf8(str("original".encode("utf-8")))))
            self.tableWidget.setItem(i*6+1, 7, QtGui.QTableWidgetItem(_fromUtf8(str("corroded".encode("utf-8")))))
            self.tableWidget.setItem(i*6+2, 7, QtGui.QTableWidgetItem(_fromUtf8(str("original".encode("utf-8")))))       
            self.tableWidget.setItem(i*6+3, 7, QtGui.QTableWidgetItem(_fromUtf8(str("corroded".encode("utf-8")))))
            self.tableWidget.setItem(i*6+4, 7, QtGui.QTableWidgetItem(_fromUtf8(str("original".encode("utf-8")))))
            self.tableWidget.setItem(i*6+5, 7, QtGui.QTableWidgetItem(_fromUtf8(str("corroded".encode("utf-8"))))) 
            
            i=i+1


    @pyqtSignature("")
    def on_btnNextStep_clicked(self):        


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
                else:
                    self.btn_Next.setText("Start")
                    self.btn_Privious.setEnabled(True)
                for i in xrange(17):
                    self.tableWidget.setItem(i,8 , QtGui.QTableWidgetItem(_fromUtf8(str("".encode("utf-8")))))    

                amount=0
                if self.mainwindow.sample_1_enable:
                    amount=amount+6
                if self.mainwindow.sample_2_enable:
                    amount=amount+6
                if self.mainwindow.sample_3_enable:
                    amount=amount+6
                self.timer_t.amount=amount
                self.timer_t.start_timer()

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

                else:
                    self.btn_Next.setText("Start")
                    self.btn_Privious.setEnabled(True)
                self.timer_t.stop()
                #self.timer.stop()
                #self.timer_t.stop()
                #self.timer.stop()
        #self.parent.close()
        #self.mainwindow.CurrentStatus="exit"
    @pyqtSignature("")
    def on_btnPrivStep_clicked(self):        
        self.parent.close()
        self.mainwindow.CurrentStatus="inputInformation"
    
    #@pyqtSignature("")
    def updateDisplay(self, text):
        #get the latest date
        #move to current position
        for i in range(10):
            time.sleep(1)
            print self.parent.mainwindow.CurrentStatus
            print "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"
    def update_timer_tv(self, value, number):
        self.tableWidget.setItem(number,8 , QtGui.QTableWidgetItem(_fromUtf8(str(str(value).encode("utf-8")))))    
        if not self.timer_t.working:
            self.btn_Next.setText("Start")
            self.btn_Privious.setEnabled(True)
        #self.timer_tv.setText(self.tr(text + " " + str(number)))

class TimeThread(QThread):
  signal_time = pyqtSignal(float, int) # 信号
 
  def __init__(self, parent=None):
    super(TimeThread, self).__init__(parent)
    self.working = True
    self.amount=0
    self.num = 0
 
  def start_timer(self):
    self.num = 0
    self.working=True

    self.start()
 
  def run(self):
    while self.working and self.num<self.amount:
    
       
      print "Working", self.thread()
      self.signal_time.emit(random.random(), self.num) # 发送信号
      self.num += 1
      self.sleep(1)
      if self.num==self.amount-1:
        self.working=False
        self.signal_time.emit(random.random(), self.num) # 发送信号

  def stop(self):
    self.working=False
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = sample_list()
    ui.show()
    sys.exit(app.exec_())
