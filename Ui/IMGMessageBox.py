# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QWidget
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QWidget, QMessageBox, QTextBrowser

from Ui_IMGMessageBox import Ui_Form

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


class IMGMessageBox(QWidget, Ui_Form):
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
        self.parent=parent
        self.setupUi(self)
        self.buttonPushed=""
    @pyqtSignature("")
    def on_btnOk_clicked(self):
        self.buttonPushed="YES"

        self.parent.close()
    @pyqtSignature("")
    def on_btnClose_clicked(self):
        self.buttonPushed="NO"
        self.parent.close()
    def showPIC(self, pciIndex):
        print pciIndex
        self.widget_bkg.setStyleSheet(_fromUtf8("#widget_bkg {background-image: url(:/fixture_slots/%s.png);}" %pciIndex))
    def setLabelTxt(self, txt):
        self.label.setText(_translate("Form", txt, None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = IMGMessageBox()
    ui.show()
    sys.exit(app.exec_())
