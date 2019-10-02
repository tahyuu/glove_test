# -*- coding: utf-8 -*-

"""
Module implementing sample_information_input.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QWidget
from PyQt4 import QtCore, QtGui
import ConfigParser
import os
import numpy as np

from Ui_sample_information_input import Ui_sample_information_input

class Sample:
    def __init__(self, slot):
        self.s_slot=slot
        self.s_name=""
        self.s_ctype=""
        self.s_mtype=""
        self.s_color=""
        self.s_thickness=""
        self.s_standard=""
        self.s_exp_time=""
        self.s_file_name=""
        self.s_firgure_img=""

        self.op1=0.0
        self.op1_list=[]
        self.rp1=0.0
        self.rp1_list=[]
        self.op2=0.0
        self.op2_list=[]
        self.rp2=0.0
        self.rp2_list=[]
        self.op3=0.0
        self.op3_list=[]
        self.rp3=0.0
        self.rp3_list=[]
        self.dr_avg=0.0
        self.avg_op=0.0
        self.avg_rp=0.0
        self.dr=0.0
        
    def calculate(self):
        #calculate dr1
        
        if self.op1>0 and self.op2>0 and self.op3>0:
            self.avg_op=(self.op1+self.op2+self.op3)/3
        if self.rp1>0 and self.rp2>0 and self.rp3>0:
            self.avg_rp=(self.rp1+self.rp2+self.rp3)/3 
        if self.avg_op>0 and self.avg_rp>0:
            self.dr=(self.avg_op- self.avg_rp)/self.avg_op

    def clean(self):
        self.op1=0.0
        self.rp1=0.0
        self.op2=0.0
        self.rp2=0.0
        self.op3=0.0
        self.rp3=0.0
        self.avg_op=0.0
        self.avg_dp=0.0
        self.dr=0.0
class sample_information_input(QWidget, Ui_sample_information_input):
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
        if self.mainwindow and not self.mainwindow.sample_1_enable:
            self.groupBox.setEnabled(False)
            self.le_1_name.setReadOnly(True)
            self.le_1_color.setReadOnly(True)
            self.cb_1_mtype.setReadOnly(True)
            self.cb_1_ctype.setReadOnly(True)
            self.le_1_thickness.setReadOnly(True)
            self.le_1_exp_time.setReadOnly(True)
        else:
            self.le_1_exp_time.setText("60")


            #self.cb_1_standard.setReadOnly(True)

        if self.mainwindow and not self.mainwindow.sample_2_enable:
            self.groupBox_2.setEnabled(False)
            self.le_2_name.setReadOnly(True)
            self.le_2_color.setReadOnly(True)
            self.cb_2_mtype.setReadOnly(True)
            self.cb_2_ctype.setReadOnly(True)
            self.le_2_thickness.setReadOnly(True)
            self.le_2_exp_time.setReadOnly(True)
        else:
            self.le_2_exp_time.setText("60")
            #self.cb_2_standard.setReadOnly(True)


        if self.mainwindow and not self.mainwindow.sample_3_enable:
            self.groupBox_3.setEnabled(False)
            self.le_3_name.setReadOnly(True)
            self.le_3_color.setReadOnly(True)
            self.le_3_mtype.setReadOnly(True)
            self.le_3_ctype.setReadOnly(True)
            self.le_3_thickness.setReadOnly(True)
            self.le_3_exp_time.setReadOnly(True)
        else:
            self.le_3_exp_time.setText("60")
            #self.cb_3_standard.setReadOnly(True)
        
        #display the inputed data
        if not self.mainwindow:
            return
        for sample in self.mainwindow.samples:
            if sample.s_slot==0:
                self.le_1_name.setText(sample.s_name)
                self.le_1_color.setText(sample.s_color)
                self.le_1_mtype.setText(sample.s_mtype)
                self.le_1_ctype.setText(sample.s_ctype)
                self.le_1_thickness.setText(sample.s_thickness)
                self.le_1_exp_time.setText(sample.s_exp_time)
            if sample.s_slot==1:
                self.le_2_name.setText(sample.s_name)
                self.le_2_color.setText(sample.s_color)
                self.le_2_mtype.setText(sample.s_mtype)
                self.le_2_ctype.setText(sample.s_ctype)
                self.le_2_thickness.setText(sample.s_thickness)
                self.le_2_exp_time.setText(sample.s_exp_time)
            if sample.s_slot==2:
                self.le_3_name.setText(sample.s_name)
                self.le_3_color.setText(sample.s_color)
                self.le_3_mtype.setText(sample.s_mtype)
                self.le_3_ctype.setText(sample.s_ctype)
                self.le_3_thickness.setText(sample.s_thickness)
                self.le_3_exp_time.setText(sample.s_exp_time)
                
                
                
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
        debug_status = self.cf.get('SysConfig', 'Debug_Input')
        if debug_status=="True":
            self.Debug=True
        else:
            self.Debug=False
        if self.Debug==True:
            for i in xrange(3):
                if i==0:
                    self.le_1_name.setText("Test name")
                    self.le_1_color.setText("Pink")
                    self.le_1_mtype.setText("Test type")
                    self.le_1_ctype.setText("test chemical")
                    self.le_1_thickness.setText("test thick ness")
                    self.le_1_exp_time.setText("60")
                if i==1:
                    self.le_2_name.setText("Test name")
                    self.le_2_color.setText("Pink")
                    self.le_2_mtype.setText("Test type")
                    self.le_2_ctype.setText("test chemical")
                    self.le_2_thickness.setText("test thick ness")
                    self.le_2_exp_time.setText("60")
                if i==2:
                    self.le_3_name.setText("Test name")
                    self.le_3_color.setText("Pink")
                    self.le_3_mtype.setText("Test type")
                    self.le_3_ctype.setText("test chemical")
                    self.le_3_thickness.setText("test thick ness")
                    self.le_3_exp_time.setText("60")

    @pyqtSignature("")
    def on_btnNextStep_clicked(self):
        self.mainwindow.nextpushed=True

        self.mainwindow.samples=[]
        if self.mainwindow.sample_1_enable:
            if self.le_1_name.text()=="":
                self.le_1_name.setFocus()
                QtGui.QMessageBox.critical(self.parent, 'Error', 'Sample 1 Name can\'t be empty!', 0,0)
                return 
            if self.le_1_color.text()=="":
                self.le_1_color.setFocus()
                QtGui.QMessageBox.critical(self.parent, 'Error', 'Sample 1 Color can\'t be empty!', 0,0) 
                return 
            if self.le_1_mtype.text()=="":
                self.le_1_mtype.setFocus()
                QtGui.QMessageBox.critical(self.parent, 'Error', 'Sample 1 Meterial Type can\'t be empty!', 0,0) 
                return 
            if self.le_1_ctype.text()=="":
                self.le_1_ctype.setFocus()
                QtGui.QMessageBox.critical(self.parent, 'Error', 'Sample 1 Chemistry can\'t be empty!', 0,0) 
                return 
            if self.le_1_thickness.text()=="":
                self.le_1_thickness.setFocus()

                QtGui.QMessageBox.critical(self.parent, 'Error', 'Sample 1 Thickness can\'t be empty!', 0,0) 
                return 
            if self.le_1_exp_time.text()=="":
                self.le_1_exp_time.setFocus()

                QtGui.QMessageBox.critical(self.parent, 'Error', 'Sample 1 Expsed Time can\'t be empty!', 0,0) 
                return 
            sample=Sample(0)
            sample.s_name=self.le_1_name.text()
            sample.s_color=self.le_1_color.text()
            sample.s_mtype=self.le_1_mtype.text()
            sample.s_ctype=self.le_1_ctype.text()
            sample.s_thickness=self.le_1_thickness.text()
            sample.s_standard=self.cb_1_standard.currentText()
            sample.s_exp_time=self.le_1_exp_time.text()

            self.mainwindow.samples.append(sample)
        if self.mainwindow.sample_2_enable:
            if self.le_2_name.text()=="":
                self.le_2_name.setFocus()

                QtGui.QMessageBox.critical(self.parent, 'Error', 'Sample 2 Name can\'t be empty!', 0,0)
                return 
            if self.le_2_color.text()=="":
                self.le_2_color.setFocus()

                QtGui.QMessageBox.critical(self.parent, 'Error', 'Sample 2 Color can\'t be empty!', 0,0) 
                return 
            if self.le_2_mtype.text()=="":
                self.le_2_mtype.setFocus()

                QtGui.QMessageBox.critical(self.parent, 'Error', 'Sample 2 Meterial Type can\'t be empty!', 0,0) 
                return 
            if self.le_2_ctype.text()=="":
                self.le_2_ctype.setFocus()

                QtGui.QMessageBox.critical(self.parent, 'Error', 'Sample 2 Chemistry can\'t be empty!', 0,0) 
                return 
            if self.le_2_thickness.text()=="":
                self.le_2_thickness.setFocus()
                QtGui.QMessageBox.critical(self.parent, 'Error', 'Sample 2 Thickness can\'t be empty!', 0,0) 
                return 
                
            if self.le_2_exp_time.text()=="":
                self.le_2_exp_time.setFocus()

                QtGui.QMessageBox.critical(self.parent, 'Error', 'Sample 2 Expsed Time can\'t be empty!', 0,0) 
                return             
            sample=Sample(1)
            sample.s_name=self.le_2_name.text()
            sample.s_color=self.le_2_color.text()
            sample.s_mtype=self.le_2_mtype.text()
            sample.s_ctype=self.le_2_ctype.text()
            sample.s_thickness=self.le_2_thickness.text()
            sample.s_standard=self.cb_2_standard.currentText()
            sample.s_exp_time=self.le_2_exp_time.text()

            self.mainwindow.samples.append(sample)
        if self.mainwindow.sample_3_enable:
            if self.le_3_name.text()=="":
                self.le_3_name.setFocus()

                QtGui.QMessageBox.critical(self.parent, 'Error', 'Sample 3 Name can\'t be empty!', 0,0)
                return 
            if self.le_3_color.text()=="":
                self.le_3_color.setFocus()

                QtGui.QMessageBox.critical(self.parent, 'Error', 'Sample 3 Color can\'t be empty!', 0,0) 
                return 
            if self.le_3_mtype.text()=="":
                self.le_3_mtype.setFocus()

                QtGui.QMessageBox.critical(self.parent, 'Error', 'Sample 3 Meterial Type can\'t be empty!', 0,0) 
                return 
            if self.le_3_ctype.text()=="":
                self.le_3_ctype.setFocus()

                QtGui.QMessageBox.critical(self.parent, 'Error', 'Sample 3 Chemistry can\'t be empty!', 0,0) 
                return 
            if self.le_3_thickness.text()=="":
                self.le_3_thickness.setFocus()
                QtGui.QMessageBox.critical(self.parent, 'Error', 'Sample 3 Thickness can\'t be empty!', 0,0) 
                return 
            if self.le_3_exp_time.text()=="":
                self.le_3_exp_time.setFocus()

                QtGui.QMessageBox.critical(self.parent, 'Error', 'Sample 3 Expsed Time can\'t be empty!', 0,0) 
                return    
            sample=Sample(2)
            sample.s_name=self.le_3_name.text()
            sample.s_color=self.le_3_color.text()
            sample.s_mtype=self.le_3_mtype.text()
            sample.s_ctype=self.le_3_ctype.text()
            sample.s_thickness=self.le_3_thickness.text()
            sample.s_standard=self.cb_3_standard.currentText()
            sample.s_exp_time=self.le_3_exp_time.text()

            self.mainwindow.samples.append(sample)
        self.parent.close()
        self.mainwindow.CurrentStatus="sample_list"
    @pyqtSignature("")
    def on_btnPrivStep_clicked(self):
        self.mainwindow.nextpushed=True        
        self.parent.close()
        self.mainwindow.CurrentStatus="selectSampels"
        
#    def closeEvent(self,event):
#
#        reply = QtGui.QMessageBox.question(self,'Message',"Are you sure to quit?", QtGui.QMessageBox.Yes|QtGui.QMessageBox.No, QtGui.QMessageBox.No)
#
#        if reply == QtGui.QMessageBox.Yes:
#            event.accept()
#        else:
#            event.ignore()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = sample_information_input()
    ui.show()
    sys.exit(app.exec_())
