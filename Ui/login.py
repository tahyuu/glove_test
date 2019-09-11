# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog

from .Ui_login import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    @pyqtSignature("")
    def on_btnHello_clicked(self):
        self.lblHello.setText("你好，PyQt4")
