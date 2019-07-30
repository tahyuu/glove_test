# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\yong\Desktop\glove_test\Ui\sample_select.ui'
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

class Ui_sample_select(object):
    def setupUi(self, sample_select):
        sample_select.setObjectName(_fromUtf8("sample_select"))
        sample_select.resize(463, 165)
        self.next_step = QtGui.QPushButton(sample_select)
        self.next_step.setGeometry(QtCore.QRect(310, 110, 141, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        self.next_step.setFont(font)
        self.next_step.setObjectName(_fromUtf8("next_step"))
        self.checkBox_3 = QtGui.QCheckBox(sample_select)
        self.checkBox_3.setGeometry(QtCore.QRect(280, 50, 111, 61))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_1 = QtGui.QCheckBox(sample_select)
        self.checkBox_1.setGeometry(QtCore.QRect(40, 50, 131, 61))
        self.checkBox_1.setObjectName(_fromUtf8("checkBox_1"))
        self.checkBox_2 = QtGui.QCheckBox(sample_select)
        self.checkBox_2.setGeometry(QtCore.QRect(160, 50, 111, 61))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.label = QtGui.QLabel(sample_select)
        self.label.setGeometry(QtCore.QRect(10, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(sample_select)
        QtCore.QObject.connect(self.next_step, QtCore.SIGNAL(_fromUtf8("clicked()")), sample_select.NextStep)
        QtCore.QMetaObject.connectSlotsByName(sample_select)

    def retranslateUi(self, sample_select):
        sample_select.setWindowTitle(_translate("sample_select", "Form", None))
        self.next_step.setText(_translate("sample_select", "Next Step", None))
        self.checkBox_3.setText(_translate("sample_select", "Sample3", None))
        self.checkBox_1.setText(_translate("sample_select", "Sample1", None))
        self.checkBox_2.setText(_translate("sample_select", "Sample2", None))
        self.label.setText(_translate("sample_select", "Step1:  Select test samples", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    sample_select = QtGui.QWidget()
    ui = Ui_sample_select()
    ui.setupUi(sample_select)
    sample_select.show()
    sys.exit(app.exec_())

