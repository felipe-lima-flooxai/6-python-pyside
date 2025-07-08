# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'workerui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(691, 505)
        font = QFont()
        font.setPointSize(40)
        Form.setFont(font)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label2 = QLabel(Form)
        self.label2.setObjectName(u"label2")

        self.gridLayout.addWidget(self.label2, 0, 1, 1, 1)

        self.label1 = QLabel(Form)
        self.label1.setObjectName(u"label1")

        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)

        self.button1 = QPushButton(Form)
        self.button1.setObjectName(u"button1")

        self.gridLayout.addWidget(self.button1, 1, 0, 1, 1)

        self.button2 = QPushButton(Form)
        self.button2.setObjectName(u"button2")

        self.gridLayout.addWidget(self.button2, 1, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label2.setText(QCoreApplication.translate("Form", u"L2", None))
        self.label1.setText(QCoreApplication.translate("Form", u"L1", None))
        self.button1.setText(QCoreApplication.translate("Form", u"B1", None))
        self.button2.setText(QCoreApplication.translate("Form", u"B2", None))
    # retranslateUi

