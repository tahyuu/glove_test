# -*- coding: utf-8 -*-

"""
Module implementing Test_W.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog

from .Ui_test import Ui_Test_W


class Test_W(QDialog, Ui_Test_W):
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
