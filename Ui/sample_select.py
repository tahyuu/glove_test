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

    @pyqtSignature("")
    def NextStep(self):
        self.parent.close()
        self.mainwindow.CurrentStatus="inputInformation"
        #print  self.parent.CurrentStatus
        if self.checkBox_1.isChecked():
            self.mainwindow.sample_1_enable=True
        if self.checkBox_2.isChecked():
            self.mainwindow.sample_2_enable=True
        if self.checkBox_3.isChecked():
            self.mainwindow.sample_3_enable=True
        
        
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = sample_select()
    ui.show()
    sys.exit(app.exec_())
