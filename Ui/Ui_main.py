# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\WorkSpace\gloves_test\Program\Ui\main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Ui_login import  *
from Ui_sample_select import *
from Ui_sample_information_input import *
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow=MainWindow
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1200, 700)
        self.centralWidget = QtGui.QWidget(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.samplesMenu = self.menuBar.addMenu("&Samples")
        self.usersMenu = self.menuBar.addMenu("&Users")
        createSameplsAction = self.createAction(
                "&createSamepls", self.createSamples,
                tip="Create Samples")
        LoginAction = self.createAction(
                "&Login", self.Login,
                tip="Login")
        LogoutAction = self.createAction(
                "&LogOut", self.LogOut,
                tip="LogOut")
        UserMangerAction = self.createAction(
                "&UserManager", self.Login,
                tip="Users Manager")
        self.addActions(self.samplesMenu , (createSameplsAction, ))
        self.addActions(self.usersMenu , (LoginAction,UserMangerAction ,LogoutAction ))

        self.retranslateUi(MainWindow)
        self.css_centralWidget= ("#centralWidget{\n"
"background-image:url(gloves.jpg) no-repeat;\n    width:100%;\n    height:100%;"
"}")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #self.MainWindow.setStyleSheet(_fromUtf8("#MainWindow{background-image:url(gloves.jpg) ;no-repeat;}"))

        self.centralWidget.setStyleSheet(self.css_centralWidget)
        
#        palette=QtGui.QPalette()
#        icon=QtGui.QPixmap('gloves.jpg')
#        palette.setBrush(self.centralWidget.backgroundRole(), QtGui.QBrush(icon)) #添加背景图片
#        self.centralWidget.setPalette(palette)

    def createAction(self, text, slot=None, shortcut=None, icon=None,
                     tip=None, checkable=False, signal="triggered()"):
        action = QtGui.QAction(text, self.MainWindow)
        if icon is not None:
            action.setIcon(QIcon(":/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.MainWindow.connect(action, QtCore.SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action
    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)
    def retranslateUi(self, MainWindow):
        self.userName=""
        self.passWord=""
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

    def Login(self):
        #self.CurrentStatus="selectSampels"
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog, self )
        Dialog.show()
        if Dialog.exec_():
            pass
    def LogOut(self):
        self.userName=""
        self.passWord=""
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog , self)
        Dialog.show()
        if Dialog.exec_():
            pass
    def CheckLogin(self):
        if self.userName=="" and self.passWord=="":
            print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            self.Login()
            return False
            return False
        else:
            return True
    def createSamples(self):
        self.CheckLogin()

        self.CurrentStatus="selectSampels"
#            return
        print self.CurrentStatus
        while True:
            if self.CurrentStatus=="selectSampels":
                Dialog = QtGui.QDialog()
                ui = Ui_sample_select()
                ui.setupUi(Dialog , self)
                Dialog.show()
                #self.CurrentStatus="inputInformation"
                if Dialog.exec_():
                    pass
            if self.CurrentStatus=="inputInformation":
                
                Dialog = QtGui.QDialog()
                ui = Ui_sample_information_input()
                ui.setupUi(Dialog , self)
                Dialog.show()
                #self.CurrentStatus="break"
                if Dialog.exec_():
                    pass
            if self.CurrentStatus=="exit":
                break


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv) 
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.Login()
    sys.exit(app.exec_()) 
        
