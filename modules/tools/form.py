# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pin-generator.ui'
#
# Created: Mon Jul 12 16:10:58 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PinGenerator(object):
    def setupUi(self, PinGenerator):
        PinGenerator.setObjectName("PinGenerator")
        PinGenerator.resize(925, 602)
        self.centralwidget = QtGui.QWidget(PinGenerator)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 60, 301, 511))
        self.textEdit.setObjectName("textEdit")
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(330, 240, 194, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.number_pins = QtGui.QLineEdit(self.formLayoutWidget)
        self.number_pins.setObjectName("number_pins")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.number_pins)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.start_x = QtGui.QLineEdit(self.formLayoutWidget)
        self.start_x.setObjectName("start_x")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.start_x)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.start_y = QtGui.QLineEdit(self.formLayoutWidget)
        self.start_y.setObjectName("start_y")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.start_y)
        self.label_6 = QtGui.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.direction = QtGui.QComboBox(self.formLayoutWidget)
        self.direction.setObjectName("direction")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.direction)
        self.pitch = QtGui.QLineEdit(self.formLayoutWidget)
        self.pitch.setObjectName("pitch")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.pitch)
        self.label_7 = QtGui.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_7)
        self.formLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(330, 150, 191, 71))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.pad_size_x = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.pad_size_x.setObjectName("pad_size_x")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.pad_size_x)
        self.pad_size_y = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.pad_size_y.setObjectName("pad_size_y")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.pad_size_y)
        self.generate = QtGui.QPushButton(self.centralwidget)
        self.generate.setGeometry(QtCore.QRect(360, 440, 131, 27))
        self.generate.setObjectName("generate")
        PinGenerator.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(PinGenerator)
        self.statusbar.setObjectName("statusbar")
        PinGenerator.setStatusBar(self.statusbar)

        self.retranslateUi(PinGenerator)
        QtCore.QMetaObject.connectSlotsByName(PinGenerator)

    def retranslateUi(self, PinGenerator):
        PinGenerator.setWindowTitle(QtGui.QApplication.translate("PinGenerator", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PinGenerator", "Number of Pins", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PinGenerator", "Start X", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PinGenerator", "Start Y", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("PinGenerator", "Direction", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("PinGenerator", "Pitch", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("PinGenerator", "Pad Size X", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("PinGenerator", "Pad Size Y", None, QtGui.QApplication.UnicodeUTF8))
        self.generate.setText(QtGui.QApplication.translate("PinGenerator", "Generate", None, QtGui.QApplication.UnicodeUTF8))
