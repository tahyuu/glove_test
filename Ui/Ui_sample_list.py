# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\WorkSpace\gloves_test\Program\Ui\sample_list.ui'
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

class Ui_sample_list(object):
    def setupUi(self, sample_list):
        sample_list.setObjectName(_fromUtf8("sample_list"))
        sample_list.resize(1031, 687)
        self.gridLayout = QtGui.QGridLayout(sample_list)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 20, -1, 20)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_Privious = QtGui.QPushButton(sample_list)
        self.btn_Privious.setMinimumSize(QtCore.QSize(151, 41))
        self.btn_Privious.setMaximumSize(QtCore.QSize(151, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        self.btn_Privious.setFont(font)
        self.btn_Privious.setObjectName(_fromUtf8("btn_Privious"))
        self.horizontalLayout.addWidget(self.btn_Privious)
        self.btn_Next = QtGui.QPushButton(sample_list)
        self.btn_Next.setMinimumSize(QtCore.QSize(151, 41))
        self.btn_Next.setMaximumSize(QtCore.QSize(151, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        self.btn_Next.setFont(font)
        self.btn_Next.setObjectName(_fromUtf8("btn_Next"))
        self.horizontalLayout.addWidget(self.btn_Next)
        self.btn_Export = QtGui.QPushButton(sample_list)
        self.btn_Export.setMaximumSize(QtCore.QSize(151, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setBold(True)
        font.setWeight(75)
        self.btn_Export.setFont(font)
        self.btn_Export.setObjectName(_fromUtf8("btn_Export"))
        self.horizontalLayout.addWidget(self.btn_Export)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.tableWidget = QtGui.QTableWidget(sample_list)
        self.tableWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(_fromUtf8(" text-align : center;\n"
"   height : 30px;\n"
"   border-style: outset;"))
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(18)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(10, 0, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.retranslateUi(sample_list)
        QtCore.QObject.connect(self.btn_Privious, QtCore.SIGNAL(_fromUtf8("clicked()")), sample_list.on_btnPrivStep_clicked)
        QtCore.QObject.connect(self.btn_Privious, QtCore.SIGNAL(_fromUtf8("clicked()")), sample_list.close)
        QtCore.QObject.connect(self.btn_Next, QtCore.SIGNAL(_fromUtf8("clicked()")), sample_list.on_btnNextStep_clicked)
        QtCore.QObject.connect(self.btn_Export, QtCore.SIGNAL(_fromUtf8("clicked()")), sample_list.on_btnExport_clicked)
        QtCore.QMetaObject.connectSlotsByName(sample_list)
        sample_list.setTabOrder(self.tableWidget, self.btn_Privious)

    def retranslateUi(self, sample_list):
        sample_list.setWindowTitle(_translate("sample_list", "Form", None))
        self.btn_Privious.setText(_translate("sample_list", "Privious Step", None))
        self.btn_Next.setText(_translate("sample_list", "Next Step", None))
        self.btn_Export.setText(_translate("sample_list", "Export Result", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("sample_list", "Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("sample_list", "Color", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("sample_list", "Materia", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("sample_list", "Chemistry", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("sample_list", "Thickness", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("sample_list", "Standard", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("sample_list", "Specimen", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("sample_list", "Status", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("sample_list", "APF(N)", None))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("sample_list", "DRx", None))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("sample_list", "DR", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    sample_list = QtGui.QWidget()
    ui = Ui_sample_list()
    ui.setupUi(sample_list)
    sample_list.show()
    sys.exit(app.exec_())

