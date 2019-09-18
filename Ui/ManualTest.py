# -*- coding: utf-8 -*-

"""
Module implementing ManulTest.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QWidget
from PyQt4 import QtCore, QtGui
from Ui_ManualTest import Ui_ManulTest


class ManulTest(QWidget, Ui_ManulTest):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QWidget.__init__(self, parent)
        self.setupUi(self)

    @pyqtSignature("")
    def Btn_Click_Forward(self):  
        print "XXXXXX"   
    @pyqtSignature("")
    def Btn_Click_Left(self):  
        print "XXXXXX"   
    @pyqtSignature("")
    def Btn_Click_Right(self):  
        print "XXXXXX"   
    @pyqtSignature("")
    def Btn_Click_BackWard(self):  
        print "XXXXXX"   
        
    @pyqtSignature("")
    def Btn_Click_ReturnZero(self):
        print "XXXXXX"   

    @pyqtSignature("")
    def Btn_Click_StartTest(self):
        print "XXXXXX"   


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = ManulTest()
    ui.show()
    sys.exit(app.exec_())
