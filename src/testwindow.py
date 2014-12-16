# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/testwindow.ui'
#
# Created: Thu Dec 11 14:17:53 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
	Dialog.setObjectName("Dialog")
	Dialog.resize(400, 300)
	self.horizontalLayout_2 = QtGui.QHBoxLayout(Dialog)
	self.horizontalLayout_2.setObjectName("horizontalLayout_2")
	self.horizontalLayout = QtGui.QHBoxLayout()
	self.horizontalLayout.setObjectName("horizontalLayout")
	self.pushButton = QtGui.QPushButton(Dialog)
	self.pushButton.setObjectName("pushButton")
	self.horizontalLayout.addWidget(self.pushButton)
	self.horizontalLayout_2.addLayout(self.horizontalLayout)

	self.retranslateUi(Dialog)
	QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
	Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
	self.pushButton.setText(QtGui.QApplication.translate("Dialog", "CLICK ME", None, QtGui.QApplication.UnicodeUTF8))
