# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\WorkSpace\gloves_test\Program\Ui\UpdateUser.ui'
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

class Ui_UpdatePassword(object):
    def setupUi(self, UpdatePassword):
        UpdatePassword.setObjectName(_fromUtf8("UpdatePassword"))
        UpdatePassword.resize(308, 187)
        UpdatePassword.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(UpdatePassword)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(UpdatePassword)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.le_userName = QtGui.QLineEdit(UpdatePassword)
        self.le_userName.setReadOnly(True)
        self.le_userName.setObjectName(_fromUtf8("le_userName"))
        self.gridLayout.addWidget(self.le_userName, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(UpdatePassword)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.le_password = QtGui.QLineEdit(UpdatePassword)
        self.le_password.setEchoMode(QtGui.QLineEdit.Password)
        self.le_password.setObjectName(_fromUtf8("le_password"))
        self.gridLayout.addWidget(self.le_password, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(UpdatePassword)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.le_npassword = QtGui.QLineEdit(UpdatePassword)
        self.le_npassword.setEchoMode(QtGui.QLineEdit.Password)
        self.le_npassword.setObjectName(_fromUtf8("le_npassword"))
        self.gridLayout.addWidget(self.le_npassword, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(UpdatePassword)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.le_cpassword = QtGui.QLineEdit(UpdatePassword)
        self.le_cpassword.setEchoMode(QtGui.QLineEdit.Password)
        self.le_cpassword.setObjectName(_fromUtf8("le_cpassword"))
        self.gridLayout.addWidget(self.le_cpassword, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        spacerItem = QtGui.QSpacerItem(71, 31, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(UpdatePassword)
        self.okButton.setMaximumSize(QtCore.QSize(75, 23))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.hboxlayout.addWidget(self.okButton)
        self.cancelButton = QtGui.QPushButton(UpdatePassword)
        self.cancelButton.setMaximumSize(QtCore.QSize(75, 23))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.hboxlayout.addWidget(self.cancelButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(UpdatePassword)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), UpdatePassword.accept)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), UpdatePassword.reject)
        QtCore.QMetaObject.connectSlotsByName(UpdatePassword)

    def retranslateUi(self, UpdatePassword):
        UpdatePassword.setWindowTitle(_translate("UpdatePassword", "Update Password", None))
        self.label.setText(_translate("UpdatePassword", "             User Name:", None))
        self.label_2.setText(_translate("UpdatePassword", "               Password:", None))
        self.label_3.setText(_translate("UpdatePassword", "       New Password:", None))
        self.label_4.setText(_translate("UpdatePassword", " Confirm Password:", None))
        self.okButton.setText(_translate("UpdatePassword", "&OK", None))
        self.cancelButton.setText(_translate("UpdatePassword", "&Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    UpdatePassword = QtGui.QDialog()
    ui = Ui_UpdatePassword()
    ui.setupUi(UpdatePassword)
    UpdatePassword.show()
    sys.exit(app.exec_())

