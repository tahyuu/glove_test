# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\yong\Desktop\glove_test\Ui\sample_information_input.ui'
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

class Ui_sample_information_input(object):
    def setupUi(self, sample_information_input):
        sample_information_input.setObjectName(_fromUtf8("sample_information_input"))
        sample_information_input.resize(754, 573)
        self.verticalLayout = QtGui.QVBoxLayout(sample_information_input)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_13 = QtGui.QLabel(sample_information_input)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout.addWidget(self.label_13)
        self.groupBox = QtGui.QGroupBox(sample_information_input)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.le_1_name = QtGui.QLineEdit(self.groupBox)
        self.le_1_name.setObjectName(_fromUtf8("le_1_name"))
        self.gridLayout.addWidget(self.le_1_name, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.le_1_color = QtGui.QLineEdit(self.groupBox)
        self.le_1_color.setText(_fromUtf8(""))
        self.le_1_color.setObjectName(_fromUtf8("le_1_color"))
        self.gridLayout.addWidget(self.le_1_color, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.le_1_mtype = QtGui.QLineEdit(self.groupBox)
        self.le_1_mtype.setObjectName(_fromUtf8("le_1_mtype"))
        self.gridLayout.addWidget(self.le_1_mtype, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.le_1_ctype = QtGui.QLineEdit(self.groupBox)
        self.le_1_ctype.setText(_fromUtf8(""))
        self.le_1_ctype.setObjectName(_fromUtf8("le_1_ctype"))
        self.gridLayout.addWidget(self.le_1_ctype, 1, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.le_1_thickness = QtGui.QLineEdit(self.groupBox)
        self.le_1_thickness.setText(_fromUtf8(""))
        self.le_1_thickness.setObjectName(_fromUtf8("le_1_thickness"))
        self.gridLayout.addWidget(self.le_1_thickness, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.cb_1_standard = QtGui.QComboBox(self.groupBox)
        self.cb_1_standard.setObjectName(_fromUtf8("cb_1_standard"))
        self.cb_1_standard.addItem(_fromUtf8(""))
        self.cb_1_standard.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cb_1_standard, 2, 3, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(sample_information_input)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.le_2_name = QtGui.QLineEdit(self.groupBox_2)
        self.le_2_name.setObjectName(_fromUtf8("le_2_name"))
        self.gridLayout_2.addWidget(self.le_2_name, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 0, 2, 1, 1)
        self.le_2_color = QtGui.QLineEdit(self.groupBox_2)
        self.le_2_color.setText(_fromUtf8(""))
        self.le_2_color.setObjectName(_fromUtf8("le_2_color"))
        self.gridLayout_2.addWidget(self.le_2_color, 0, 3, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.le_2_mtype = QtGui.QLineEdit(self.groupBox_2)
        self.le_2_mtype.setObjectName(_fromUtf8("le_2_mtype"))
        self.gridLayout_2.addWidget(self.le_2_mtype, 1, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 1, 2, 1, 1)
        self.le_2_ctype = QtGui.QLineEdit(self.groupBox_2)
        self.le_2_ctype.setText(_fromUtf8(""))
        self.le_2_ctype.setObjectName(_fromUtf8("le_2_ctype"))
        self.gridLayout_2.addWidget(self.le_2_ctype, 1, 3, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
        self.le_2_thickness = QtGui.QLineEdit(self.groupBox_2)
        self.le_2_thickness.setText(_fromUtf8(""))
        self.le_2_thickness.setObjectName(_fromUtf8("le_2_thickness"))
        self.gridLayout_2.addWidget(self.le_2_thickness, 2, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 2, 2, 1, 1)
        self.cb_2_standard = QtGui.QComboBox(self.groupBox_2)
        self.cb_2_standard.setObjectName(_fromUtf8("cb_2_standard"))
        self.cb_2_standard.addItem(_fromUtf8(""))
        self.cb_2_standard.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.cb_2_standard, 2, 3, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(sample_information_input)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_19 = QtGui.QLabel(self.groupBox_3)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_4.addWidget(self.label_19, 0, 0, 1, 1)
        self.le_3_name = QtGui.QLineEdit(self.groupBox_3)
        self.le_3_name.setObjectName(_fromUtf8("le_3_name"))
        self.gridLayout_4.addWidget(self.le_3_name, 0, 1, 1, 1)
        self.label_20 = QtGui.QLabel(self.groupBox_3)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_4.addWidget(self.label_20, 0, 2, 1, 1)
        self.le_3_color = QtGui.QLineEdit(self.groupBox_3)
        self.le_3_color.setText(_fromUtf8(""))
        self.le_3_color.setObjectName(_fromUtf8("le_3_color"))
        self.gridLayout_4.addWidget(self.le_3_color, 0, 3, 1, 1)
        self.label_21 = QtGui.QLabel(self.groupBox_3)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_4.addWidget(self.label_21, 1, 0, 1, 1)
        self.le_3_mtype = QtGui.QLineEdit(self.groupBox_3)
        self.le_3_mtype.setObjectName(_fromUtf8("le_3_mtype"))
        self.gridLayout_4.addWidget(self.le_3_mtype, 1, 1, 1, 1)
        self.label_22 = QtGui.QLabel(self.groupBox_3)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_4.addWidget(self.label_22, 1, 2, 1, 1)
        self.le_3_ctype = QtGui.QLineEdit(self.groupBox_3)
        self.le_3_ctype.setText(_fromUtf8(""))
        self.le_3_ctype.setObjectName(_fromUtf8("le_3_ctype"))
        self.gridLayout_4.addWidget(self.le_3_ctype, 1, 3, 1, 1)
        self.label_23 = QtGui.QLabel(self.groupBox_3)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_4.addWidget(self.label_23, 2, 0, 1, 1)
        self.le_3_thickness = QtGui.QLineEdit(self.groupBox_3)
        self.le_3_thickness.setText(_fromUtf8(""))
        self.le_3_thickness.setObjectName(_fromUtf8("le_3_thickness"))
        self.gridLayout_4.addWidget(self.le_3_thickness, 2, 1, 1, 1)
        self.label_24 = QtGui.QLabel(self.groupBox_3)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_4.addWidget(self.label_24, 2, 2, 1, 1)
        self.cb_3_standard = QtGui.QComboBox(self.groupBox_3)
        self.cb_3_standard.setObjectName(_fromUtf8("cb_3_standard"))
        self.cb_3_standard.addItem(_fromUtf8(""))
        self.cb_3_standard.addItem(_fromUtf8(""))
        self.gridLayout_4.addWidget(self.cb_3_standard, 2, 3, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_4)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.bt_last = QtGui.QPushButton(sample_information_input)
        self.bt_last.setMaximumSize(QtCore.QSize(161, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setBold(True)
        font.setWeight(75)
        self.bt_last.setFont(font)
        self.bt_last.setObjectName(_fromUtf8("bt_last"))
        self.horizontalLayout_4.addWidget(self.bt_last)
        self.bt_next = QtGui.QPushButton(sample_information_input)
        self.bt_next.setMaximumSize(QtCore.QSize(151, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setBold(True)
        font.setWeight(75)
        self.bt_next.setFont(font)
        self.bt_next.setObjectName(_fromUtf8("bt_next"))
        self.horizontalLayout_4.addWidget(self.bt_next)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(sample_information_input)
        QtCore.QObject.connect(self.bt_next, QtCore.SIGNAL(_fromUtf8("clicked()")), sample_information_input.close)
        QtCore.QObject.connect(self.bt_next, QtCore.SIGNAL(_fromUtf8("clicked()")), sample_information_input.on_btnNextStep_clicked)
        QtCore.QObject.connect(self.bt_last, QtCore.SIGNAL(_fromUtf8("clicked()")), sample_information_input.on_btnPrivStep_clicked)
        QtCore.QMetaObject.connectSlotsByName(sample_information_input)

    def retranslateUi(self, sample_information_input):
        sample_information_input.setWindowTitle(_translate("sample_information_input", "Sample information input", None))
        self.label_13.setText(_translate("sample_information_input", "Step2: Input Samples information", None))
        self.groupBox.setTitle(_translate("sample_information_input", "Information for sample 1", None))
        self.label.setText(_translate("sample_information_input", "Sample Name:", None))
        self.label_4.setText(_translate("sample_information_input", "Sample Color:", None))
        self.label_2.setText(_translate("sample_information_input", "Materia Type:", None))
        self.label_5.setText(_translate("sample_information_input", "Chemistry Type:", None))
        self.label_3.setText(_translate("sample_information_input", "Sample Thickness:", None))
        self.label_6.setText(_translate("sample_information_input", "Standard: ", None))
        self.cb_1_standard.setItemText(0, _translate("sample_information_input", "EN374-4", None))
        self.cb_1_standard.setItemText(1, _translate("sample_information_input", "Other", None))
        self.groupBox_2.setTitle(_translate("sample_information_input", "Information for sample 2", None))
        self.label_7.setText(_translate("sample_information_input", "Sample Name:", None))
        self.label_8.setText(_translate("sample_information_input", "Sample Color:", None))
        self.label_9.setText(_translate("sample_information_input", "Materia Type:", None))
        self.label_10.setText(_translate("sample_information_input", "Chemistry Type:", None))
        self.label_11.setText(_translate("sample_information_input", "Sample Thickness:", None))
        self.label_12.setText(_translate("sample_information_input", "Standard: ", None))
        self.cb_2_standard.setItemText(0, _translate("sample_information_input", "EN374-4", None))
        self.cb_2_standard.setItemText(1, _translate("sample_information_input", "Other", None))
        self.groupBox_3.setTitle(_translate("sample_information_input", "Information for sample 3", None))
        self.label_19.setText(_translate("sample_information_input", "Sample Name:", None))
        self.label_20.setText(_translate("sample_information_input", "Sample Color:", None))
        self.label_21.setText(_translate("sample_information_input", "Materia Type:", None))
        self.label_22.setText(_translate("sample_information_input", "Chemistry Type:", None))
        self.label_23.setText(_translate("sample_information_input", "Sample Thickness:", None))
        self.label_24.setText(_translate("sample_information_input", "Standard: ", None))
        self.cb_3_standard.setItemText(0, _translate("sample_information_input", "EN374-4", None))
        self.cb_3_standard.setItemText(1, _translate("sample_information_input", "Other", None))
        self.bt_last.setText(_translate("sample_information_input", "Privious Step", None))
        self.bt_next.setText(_translate("sample_information_input", "Next Step", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    sample_information_input = QtGui.QWidget()
    ui = Ui_sample_information_input()
    ui.setupUi(sample_information_input)
    sample_information_input.show()
    sys.exit(app.exec_())

