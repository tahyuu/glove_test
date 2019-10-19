# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\WorkSpace\gloves_test\Program\Ui\IMGMessageBox.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
from PyQt4.QtGui import QWidget, QMessageBox, QTextBrowser

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(678, 611)
        Form.setStyleSheet(_fromUtf8(""))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 390, 641, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bahnschrift SemiLight"))
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 540, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 540, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.widget_bkg = QtGui.QWidget(Form)
        self.widget_bkg.setGeometry(QtCore.QRect(30, 20, 621, 351))
        self.widget_bkg.setStyleSheet(_fromUtf8("background-image: url(:/fixture_slots/001.png);"))
        self.widget_bkg.setObjectName(_fromUtf8("widget_bkg"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.on_btnOk_clicked)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "<html><head/><body><p>please double confirm the test sample are loading </p><p>as above picture, </p><p>Test will start once you push the OK button</p></body></html>", None))
        self.pushButton_2.setText(_translate("Form", "Cancel", None))
        self.pushButton.setText(_translate("Form", "OK", None))
    def closeEvent(self, event):
         res=QMessageBox.question(self,'消息','是否关闭这个窗口？',QMessageBox.Yes|QMessageBox.No,QMessageBox.No) #两个按钮是否， 默认No则关闭这个提示框
         if res==QMessageBox.Yes:
             event.accept()  
         else:
             event.ignore()
import gloves_resource_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

