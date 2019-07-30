# -*- coding: utf-8 -*-

"""
Module implementing sample_information_input.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QWidget
from PyQt4 import QtCore, QtGui

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
            self.le_1_mtype.setReadOnly(True)
            self.le_1_ctype.setReadOnly(True)
            self.le_1_thickness.setReadOnly(True)
            #self.cb_1_standard.setReadOnly(True)

        if self.mainwindow and not self.mainwindow.sample_2_enable:
            self.groupBox_2.setEnabled(False)
            self.le_2_name.setReadOnly(True)
            self.le_2_color.setReadOnly(True)
            self.le_2_mtype.setReadOnly(True)
            self.le_2_ctype.setReadOnly(True)
            self.le_2_thickness.setReadOnly(True)
            #self.cb_2_standard.setReadOnly(True)


        if self.mainwindow and not self.mainwindow.sample_3_enable:
            self.groupBox_3.setEnabled(False)
            self.le_3_name.setReadOnly(True)
            self.le_3_color.setReadOnly(True)
            self.le_3_mtype.setReadOnly(True)
            self.le_3_ctype.setReadOnly(True)
            self.le_3_thickness.setReadOnly(True)
            #self.cb_3_standard.setReadOnly(True)
        
        #display the inputed data
        for sample in self.mainwindow.samples:
            if sample.s_slot==0:
                self.le_1_name.setText(sample.s_name)
                self.le_1_color.setText(sample.s_color)
                self.le_1_mtype.setText(sample.s_mtype)
                self.le_1_ctype.setText(sample.s_ctype)
                self.le_1_thickness.setText(sample.s_thickness)

            if sample.s_slot==1:
                self.le_2_name.setText(sample.s_name)
                self.le_2_color.setText(sample.s_color)
                self.le_2_mtype.setText(sample.s_mtype)
                self.le_2_ctype.setText(sample.s_ctype)
                self.le_2_thickness.setText(sample.s_thickness)

            if sample.s_slot==2:
                self.le_3_name.setText(sample.s_name)
                self.le_3_color.setText(sample.s_color)
                self.le_3_mtype.setText(sample.s_mtype)
                self.le_3_ctype.setText(sample.s_ctype)
                self.le_3_thickness.setText(sample.s_thickness)

    @pyqtSignature("")
    def on_btnNextStep_clicked(self):
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
            sample=Sample(0)
            sample.s_name=self.le_1_name.text()
            sample.s_color=self.le_1_color.text()
            sample.s_mtype=self.le_1_mtype.text()
            sample.s_ctype=self.le_1_ctype.text()
            sample.s_thickness=self.le_1_thickness.text()
            sample.s_standard=self.cb_1_standard.currentText()

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
            sample=Sample(1)
            sample.s_name=self.le_2_name.text()
            sample.s_color=self.le_2_color.text()
            sample.s_mtype=self.le_2_mtype.text()
            sample.s_ctype=self.le_2_ctype.text()
            sample.s_thickness=self.le_2_thickness.text()
            sample.s_standard=self.cb_2_standard.currentText()

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
            sample=Sample(2)
            sample.s_name=self.le_3_name.text()
            sample.s_color=self.le_3_color.text()
            sample.s_mtype=self.le_3_mtype.text()
            sample.s_ctype=self.le_3_ctype.text()
            sample.s_thickness=self.le_3_thickness.text()
            sample.s_standard=self.cb_3_standard.currentText()

            self.mainwindow.samples.append(sample)
        self.parent.close()
        self.mainwindow.CurrentStatus="sample_list"
    @pyqtSignature("")
    def on_btnPrivStep_clicked(self):        
        self.parent.close()
        self.mainwindow.CurrentStatus="selectSampels"

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = sample_information_input()
    ui.show()
    sys.exit(app.exec_())
