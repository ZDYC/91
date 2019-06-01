# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_porn91(object):
    def setupUi(self, porn91):
        porn91.setObjectName("porn91")
        porn91.resize(800, 498)
        self.centralwidget = QtWidgets.QWidget(porn91)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 4, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 49, 781, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(690, 0, 111, 41))
        self.toolButton.setObjectName("toolButton")
        porn91.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(porn91)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        porn91.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(porn91)
        self.statusbar.setObjectName("statusbar")
        porn91.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(porn91)
        self.toolBar.setObjectName("toolBar")
        porn91.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(porn91)
        self.toolBar_2.setObjectName("toolBar_2")
        porn91.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)

        self.retranslateUi(porn91)
        QtCore.QMetaObject.connectSlotsByName(porn91)

    def retranslateUi(self, porn91):
        _translate = QtCore.QCoreApplication.translate
        porn91.setWindowTitle(_translate("porn91", "MainWindow"))
        self.pushButton.setText(_translate("porn91", "start"))
        self.toolButton.setText(_translate("porn91", "proxy"))
        self.toolBar.setWindowTitle(_translate("porn91", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("porn91", "toolBar_2"))



if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = Ui_porn91()
    myshow.show()
    sys.exit(app.exec_())


