# -*- coding: utf-8 -*-

"""
Module implementing sample_select.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QWidget
from PyQt4 import QtCore, QtGui

from Ui_sample_select import Ui_sample_select


class sample_select(QWidget, Ui_sample_select):
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
        self.mainwindow=mainwindow
        self.parent=parent
        self.setupUi(self)
        if self.mainwindow:
            if self.mainwindow.sample_1_enable:
                self.checkBox_1.setCheckState(2)
            if self.mainwindow.sample_2_enable:
                self.checkBox_2.setCheckState(2)
            if self.mainwindow.sample_3_enable:
                self.checkBox_3.setCheckState(2)

    @pyqtSignature("")
    def NextStep(self):
        self.mainwindow.nextpushed=True
        self.parent.close()
        #print  self.parent.CurrentStatus
        if self.checkBox_1.isChecked():
            self.mainwindow.sample_1_enable=True
        else:
            self.mainwindow.sample_1_enable=False
            
        if self.checkBox_2.isChecked():
            self.mainwindow.sample_2_enable=True
        else:
            self.mainwindow.sample_2_enable=False

        if self.checkBox_3.isChecked():
            self.mainwindow.sample_3_enable=True
        else:
            self.mainwindow.sample_3_enable=False
            
        #to remove sample which not selected from sample list
        tmp_samples=[]
        for sample in self.mainwindow.samples:
            if sample.s_slot==0 and  self.mainwindow.sample_1_enable:
                tmp_samples.append(sample)
            if sample.s_slot==1 and self.mainwindow.sample_2_enable:
                tmp_samples.append(sample)
            if sample.s_slot==2 and self.mainwindow.sample_3_enable:
                tmp_samples.append(sample)
        self.mainwindow.samples=tmp_samples
        self.mainwindow.CurrentStatus="inputInformation"
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
    ui = sample_select()
    ui.show()
    sys.exit(app.exec_())
