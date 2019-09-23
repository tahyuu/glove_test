# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\WorkSpace\gloves_test\Program\Ui\login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import ConfigParser
import os
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

class Ui_Login(object):
    def setupUi(self, Dialog, parent):
        self.Dialog=Dialog
        self.parent=parent
        Dialog.setObjectName(_fromUtf8("Login"))
        Dialog.resize(320, 153)
        Dialog.setSizeGripEnabled(True)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 120, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 120, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 30, 123, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 70, 123, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password) 

        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Login)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.cf=ConfigParser.ConfigParser()
        currentDir=os.getcwd()
        #print currentDir
        self.cf.read("%s\Config.ini" %currentDir)
        ######################################
        #to get debug Stutu3 in SysConfig Debug
        ######################################
        debug_status = self.cf.get('SysConfig', 'Debug_Input')
        if debug_status=="True":
            self.Debug=True
        else:
            self.Debug=False
        if self.Debug==True:
            self.lineEdit.setText("admin")
            self.lineEdit_2.setText("admin")

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Login", "Login", None))
        self.label.setText(_translate("Login", "User Name:", None))
        self.label_2.setText(_translate("Login", " Password:", None))
        self.pushButton.setText(_translate("Dialog", "Login", None))
    def Login(self):
        Login_Status=False
        userName = self.lineEdit.text()
        passWord = self.lineEdit_2.text()
        for (Key, value) in self.cf.items("UserConfig"):
            if value.find("|")>0 and value.split("|")[0]==userName and passWord==value.split("|")[1]:
                Login_Status=True
                break
            #print value
        if Login_Status: 
                self.parent.userName=userName
                self.parent.passWord=passWord
                self.Dialog.close()
        else: 
            QtGui.QMessageBox.critical(self.Dialog, 'Error', 'User name or password not correct!', 0,0) 
 
        


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Login()
    ui.setupUi(Dialog, None)
    Dialog.show()
    sys.exit(app.exec_())

