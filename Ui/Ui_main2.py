# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\WorkSpace\gloves_test\Program\Ui\main2'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("background-image:url(gloves.jpg) ;no-repeat;\n"
"filter:\"progid:DXImageTransform.Microsoft.AlphaImageLoader(sizingMethod=\'scale\')\";  \n"
"-moz-background-size:100% 100%;  \n"
"    background-size:100% 100%; "))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuSample = QtGui.QMenu(self.menuBar)
        self.menuSample.setObjectName(_fromUtf8("menuSample"))
        self.menuUsers = QtGui.QMenu(self.menuBar)
        self.menuUsers.setObjectName(_fromUtf8("menuUsers"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionCreate_Samples = QtGui.QAction(MainWindow)
        self.actionCreate_Samples.setObjectName(_fromUtf8("actionCreate_Samples"))
        self.actionLogin = QtGui.QAction(MainWindow)
        self.actionLogin.setObjectName(_fromUtf8("actionLogin"))
        self.actionCreate_User = QtGui.QAction(MainWindow)
        self.actionCreate_User.setObjectName(_fromUtf8("actionCreate_User"))
        self.menuSample.addAction(self.actionCreate_Samples)
        self.menuUsers.addSeparator()
        self.menuUsers.addAction(self.actionLogin)
        self.menuUsers.addAction(self.actionCreate_User)
        self.menuBar.addAction(self.menuSample.menuAction())
        self.menuBar.addAction(self.menuUsers.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuSample.setTitle(_translate("MainWindow", "Sample", None))
        self.menuUsers.setTitle(_translate("MainWindow", "Users", None))
        self.actionCreate_Samples.setText(_translate("MainWindow", "Create Samples", None))
        self.actionLogin.setText(_translate("MainWindow", "Login", None))
        self.actionCreate_User.setText(_translate("MainWindow", "User Manager", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

