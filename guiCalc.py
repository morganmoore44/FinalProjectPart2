# Form implementation generated from reading ui file 'guiCalc.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(429, 606)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.name_input = QtWidgets.QLineEdit(parent=Form)
        self.name_input.setGeometry(QtCore.QRect(280, 50, 113, 22))
        self.name_input.setObjectName("name_input")
        self.income_input = QtWidgets.QLineEdit(parent=Form)
        self.income_input.setGeometry(QtCore.QRect(280, 90, 113, 22))
        self.income_input.setObjectName("income_input")
        self.needs_input = QtWidgets.QLineEdit(parent=Form)
        self.needs_input.setGeometry(QtCore.QRect(280, 130, 113, 22))
        self.needs_input.setObjectName("needs_input")
        self.wants_input = QtWidgets.QLineEdit(parent=Form)
        self.wants_input.setGeometry(QtCore.QRect(280, 170, 113, 22))
        self.wants_input.setObjectName("wants_input")
        self.savings_input = QtWidgets.QLineEdit(parent=Form)
        self.savings_input.setGeometry(QtCore.QRect(280, 210, 113, 22))
        self.savings_input.setObjectName("savings_input")
        self.output_label = QtWidgets.QLabel(parent=Form)
        self.output_label.setGeometry(QtCore.QRect(40, 310, 341, 241))
        self.output_label.setText("")
        self.output_label.setObjectName("output_label")
        self.name_label = QtWidgets.QLabel(parent=Form)
        self.name_label.setGeometry(QtCore.QRect(10, 50, 191, 16))
        self.name_label.setObjectName("name_label")
        self.income_label = QtWidgets.QLabel(parent=Form)
        self.income_label.setGeometry(QtCore.QRect(10, 90, 231, 16))
        self.income_label.setObjectName("income_label")
        self.needs_label = QtWidgets.QLabel(parent=Form)
        self.needs_label.setGeometry(QtCore.QRect(10, 130, 271, 16))
        self.needs_label.setObjectName("needs_label")
        self.wants_label = QtWidgets.QLabel(parent=Form)
        self.wants_label.setGeometry(QtCore.QRect(10, 170, 271, 16))
        self.wants_label.setObjectName("wants_label")
        self.savings_label = QtWidgets.QLabel(parent=Form)
        self.savings_label.setGeometry(QtCore.QRect(10, 210, 271, 16))
        self.savings_label.setObjectName("savings_label")
        self.title_label = QtWidgets.QLabel(parent=Form)
        self.title_label.setGeometry(QtCore.QRect(150, 10, 261, 21))
        self.title_label.setObjectName("title_label")
        self.submit_button = QtWidgets.QPushButton(parent=Form)
        self.submit_button.setGeometry(QtCore.QRect(170, 250, 80, 26))
        self.submit_button.setObjectName("submit_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "BudgetCalculator"))
        self.name_label.setText(_translate("Form", "Enter your name:"))
        self.income_label.setText(_translate("Form", "Enter your total income after taxes:"))
        self.needs_label.setText(_translate("Form", "Enter needs total: (Housing, food, bills, etc.)"))
        self.wants_label.setText(_translate("Form", "Enter wants total: (Eating out, shopping, etc.)"))
        self.savings_label.setText(_translate("Form", "Enter savings total: "))
        self.title_label.setText(_translate("Form", "Budget Rating Calculator"))
        self.submit_button.setText(_translate("Form", "Submit"))


