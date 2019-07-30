# -*- coding: utf-8 -*-

"""
Module implementing sample_information_input.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QWidget
from PyQt4 import QtCore, QtGui
from Ui_sample_information_input import Ui_sample_information_input


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
        
    @pyqtSignature("")
    def on_btnNextStep_clicked(self):        
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
