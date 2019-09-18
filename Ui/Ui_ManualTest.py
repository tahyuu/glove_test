# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\WorkSpace\gloves_test\Program\Ui\ManualTest.ui'
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

class Ui_ManulTest(object):
    def setupUi(self, ManulTest):
        ManulTest.setObjectName(_fromUtf8("ManulTest"))
        ManulTest.resize(806, 801)
        self.verticalLayout = QtGui.QVBoxLayout(ManulTest)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(ManulTest)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.groupBox_3 = QtGui.QGroupBox(ManulTest)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 80))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.Btn_Return_Zero = QtGui.QPushButton(self.groupBox_3)
        self.Btn_Return_Zero.setMinimumSize(QtCore.QSize(0, 50))
        self.Btn_Return_Zero.setMaximumSize(QtCore.QSize(81, 50))
        self.Btn_Return_Zero.setObjectName(_fromUtf8("Btn_Return_Zero"))
        self.horizontalLayout_2.addWidget(self.Btn_Return_Zero)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox = QtGui.QGroupBox(ManulTest)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 261))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 261))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.widget = QtGui.QWidget(self.groupBox)
        self.widget.setMaximumSize(QtCore.QSize(371, 231))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Btn_Forward = QtGui.QPushButton(self.widget)
        self.Btn_Forward.setMaximumSize(QtCore.QSize(81, 51))
        self.Btn_Forward.setObjectName(_fromUtf8("Btn_Forward"))
        self.gridLayout.addWidget(self.Btn_Forward, 0, 1, 1, 1)
        self.Btn_Left = QtGui.QPushButton(self.widget)
        self.Btn_Left.setMaximumSize(QtCore.QSize(81, 51))
        self.Btn_Left.setObjectName(_fromUtf8("Btn_Left"))
        self.gridLayout.addWidget(self.Btn_Left, 1, 0, 1, 1)
        self.Btn_backward = QtGui.QPushButton(self.widget)
        self.Btn_backward.setMaximumSize(QtCore.QSize(81, 51))
        self.Btn_backward.setObjectName(_fromUtf8("Btn_backward"))
        self.gridLayout.addWidget(self.Btn_backward, 2, 1, 1, 1)
        self.Btn_Right = QtGui.QPushButton(self.widget)
        self.Btn_Right.setMaximumSize(QtCore.QSize(81, 51))
        self.Btn_Right.setObjectName(_fromUtf8("Btn_Right"))
        self.gridLayout.addWidget(self.Btn_Right, 1, 2, 1, 1)
        self.Le_XY_speed = QtGui.QLineEdit(self.widget)
        self.Le_XY_speed.setMaximumSize(QtCore.QSize(81, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Le_XY_speed.setFont(font)
        self.Le_XY_speed.setObjectName(_fromUtf8("Le_XY_speed"))
        self.gridLayout.addWidget(self.Le_XY_speed, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(ManulTest)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 253))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.graphicsView = QtGui.QGraphicsView(self.groupBox_2)
        self.graphicsView.setMaximumSize(QtCore.QSize(16777215, 231))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout_2.addWidget(self.graphicsView, 1, 0, 1, 4)
        self.Btn_Start = QtGui.QPushButton(self.groupBox_2)
        self.Btn_Start.setMinimumSize(QtCore.QSize(0, 50))
        self.Btn_Start.setMaximumSize(QtCore.QSize(150, 90))
        self.Btn_Start.setObjectName(_fromUtf8("Btn_Start"))
        self.gridLayout_2.addWidget(self.Btn_Start, 0, 2, 1, 1)
        self.lcdNumber = QtGui.QLCDNumber(self.groupBox_2)
        self.lcdNumber.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.gridLayout_2.addWidget(self.lcdNumber, 0, 3, 1, 1)
        self.Le_Max_Limit = QtGui.QLineEdit(self.groupBox_2)
        self.Le_Max_Limit.setMinimumSize(QtCore.QSize(100, 50))
        self.Le_Max_Limit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.Le_Max_Limit.setObjectName(_fromUtf8("Le_Max_Limit"))
        self.gridLayout_2.addWidget(self.Le_Max_Limit, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(ManulTest)
        QtCore.QObject.connect(self.Btn_Forward, QtCore.SIGNAL(_fromUtf8("clicked()")), ManulTest.Btn_Click_Forward)
        QtCore.QObject.connect(self.Btn_Left, QtCore.SIGNAL(_fromUtf8("clicked()")), ManulTest.Btn_Click_Left)
        QtCore.QObject.connect(self.Btn_Right, QtCore.SIGNAL(_fromUtf8("clicked()")), ManulTest.Btn_Click_Right)
        QtCore.QObject.connect(self.Btn_backward, QtCore.SIGNAL(_fromUtf8("clicked()")), ManulTest.Btn_Click_BackWard)
        QtCore.QObject.connect(self.Btn_Return_Zero, QtCore.SIGNAL(_fromUtf8("clicked()")), ManulTest.Btn_Click_ReturnZero)
        QtCore.QObject.connect(self.Btn_Start, QtCore.SIGNAL(_fromUtf8("clicked()")), ManulTest.Btn_Click_StartTest)
        QtCore.QMetaObject.connectSlotsByName(ManulTest)

    def retranslateUi(self, ManulTest):
        ManulTest.setWindowTitle(_translate("ManulTest", "Muanul Test", None))
        self.label_3.setText(_translate("ManulTest", "Manual Test Step:\n"
"    1, adjust the fixture to right opsition with X/Y Axis Buttons\n"
"    2, Click the Down Button to get the Punctual value", None))
        self.groupBox_3.setTitle(_translate("ManulTest", "Return Zero", None))
        self.label_4.setText(_translate("ManulTest", "Push Return Zero button to reutn Zero:", None))
        self.Btn_Return_Zero.setText(_translate("ManulTest", "Return Zero", None))
        self.groupBox.setTitle(_translate("ManulTest", "X/Y Axis ", None))
        self.label.setText(_translate("ManulTest", "X/Y  Axis：", None))
        self.Btn_Forward.setText(_translate("ManulTest", "forward ", None))
        self.Btn_Left.setText(_translate("ManulTest", "Left", None))
        self.Btn_backward.setText(_translate("ManulTest", "backward", None))
        self.Btn_Right.setText(_translate("ManulTest", "right", None))
        self.Le_XY_speed.setText(_translate("ManulTest", "111", None))
        self.groupBox_2.setTitle(_translate("ManulTest", "Z Axis", None))
        self.label_2.setText(_translate("ManulTest", "Z  Axis：", None))
        self.Btn_Start.setText(_translate("ManulTest", "Start Get Puncual", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ManulTest = QtGui.QWidget()
    ui = Ui_ManulTest()
    ui.setupUi(ManulTest)
    ManulTest.show()
    sys.exit(app.exec_())

