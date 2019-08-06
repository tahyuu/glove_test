# -*- coding: utf-8 -*-

"""
Module implementing UpdatePassword.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QWidget
from PyQt4 import QtCore, QtGui

from Ui_UpdatePassword import Ui_UpdatePassword


class UpdatePassword(QWidget, Ui_UpdatePassword):
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
        self.mainwindow=mainwindow
        self.parent=parent
        self.le_userName.setText(self.mainwindow.userName)
    @pyqtSignature("")
    def btn_Ok_UpdatePassword(self):
        if self.le_userName.text()=="":
            self.le_userName.setFocus()
            QtGui.QMessageBox.critical(self.parent, 'Error', 'user Name can\'t be empty', 0,0) 
            return
        if self.le_password.text()=="" or self.le_password.text()!=self.mainwindow.passWord:
            self.le_password.setFocus()
            QtGui.QMessageBox.critical(self.parent, 'Error', 'Your password not correct! please try again', 0,0) 
            return
        if self.le_npassword.text()=="":
            self.le_npassword.setFocus()
            QtGui.QMessageBox.critical(self.parent, 'Error', 'New Password can\'t be empty', 0,0) 
            return
        if self.le_cpassword.text()=="":
            self.le_cpassword.setFocus()
            QtGui.QMessageBox.critical(self.parent, 'Error', 'Confirm new password can\'t be empty', 0,0) 
            return
        if self.le_cpassword.text()!=self.le_npassword.text():
            self.le_cpassword.setFocus()
            QtGui.QMessageBox.critical(self.parent, 'Error', 'please make sure \'confirm new password\' are same as \'New Password\'!', 0,0) 
            return
        #update the password code update here
        #QtGui.QMessageBox.critical(self.parent, 'Error', 'please make sure \'confirm new password\' are same as \'New Password\'!', 0,0) 
        QtGui.QMessageBox.information(self.parent,"Message","Password Update success!",QtGui.QMessageBox.Yes,QtGui.QMessageBox.Yes)
        self.parent.close()
        self.mainwindow.userName="" 
        self.mainwindow.passWord="" 
        self.mainwindow.CheckLogin()
    @pyqtSignature("")
    def btn_Cancel_close(self):
        self.parent.close()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = UpdatePassword()
    ui.show()
    sys.exit(app.exec_())
