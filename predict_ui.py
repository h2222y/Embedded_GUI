# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'predict.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QWidget)

class Ui_MyWindow(object):
    def setupUi(self, MyWindow):
        if not MyWindow.objectName():
            MyWindow.setObjectName(u"MyWindow")
        MyWindow.resize(800, 600)
        self.checkAction = QAction(MyWindow)
        self.checkAction.setObjectName(u"checkAction")
        self.byeAction = QAction(MyWindow)
        self.byeAction.setObjectName(u"byeAction")
        self.centralwidget = QWidget(MyWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 95, 71, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 136, 71, 21))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 178, 71, 21))
        self.textBox1 = QLineEdit(self.centralwidget)
        self.textBox1.setObjectName(u"textBox1")
        self.textBox1.setGeometry(QRect(150, 90, 121, 31))
        self.textBox2 = QLineEdit(self.centralwidget)
        self.textBox2.setObjectName(u"textBox2")
        self.textBox2.setGeometry(QRect(150, 130, 121, 31))
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(150, 174, 121, 31))
        self.spinBox.setValue(25)
        self.btn1 = QPushButton(self.centralwidget)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setGeometry(QRect(90, 220, 181, 51))
        self.btn2 = QPushButton(self.centralwidget)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setGeometry(QRect(90, 280, 181, 51))
        MyWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MyWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MyWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MyWindow)
        self.statusbar.setObjectName(u"statusbar")
        MyWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.checkAction)
        self.menuFile.addAction(self.byeAction)

        self.retranslateUi(MyWindow)
        self.btn1.clicked.connect(MyWindow.check)
        self.btn2.clicked.connect(MyWindow.clear)
        self.checkAction.triggered.connect(MyWindow.check)
        self.byeAction.triggered.connect(MyWindow.bye)

        QMetaObject.connectSlotsByName(MyWindow)
    # setupUi

    def retranslateUi(self, MyWindow):
        MyWindow.setWindowTitle(QCoreApplication.translate("MyWindow", u"MainWindow", None))
        self.checkAction.setText(QCoreApplication.translate("MyWindow", u"\uacb0\uacfc \ud655\uc778", None))
        self.byeAction.setText(QCoreApplication.translate("MyWindow", u"\uc885\ub8cc", None))
        self.label.setText(QCoreApplication.translate("MyWindow", u"\ubcf8\uc778 :", None))
        self.label_2.setText(QCoreApplication.translate("MyWindow", u"\uc0c1\ub300 :", None))
        self.label_3.setText(QCoreApplication.translate("MyWindow", u"\uc0c1\ub300\ub098\uc774 :", None))
        self.textBox1.setText(QCoreApplication.translate("MyWindow", u"\uae40\ud61c\uc218", None))
        self.textBox2.setText(QCoreApplication.translate("MyWindow", u"\uc1a1\uc911\uae30", None))
        self.btn1.setText(QCoreApplication.translate("MyWindow", u"\uacb0\uacfc\ud655\uc778", None))
        self.btn2.setText(QCoreApplication.translate("MyWindow", u"Clear", None))
        self.menuFile.setTitle(QCoreApplication.translate("MyWindow", u"File", None))
    # retranslateUi

