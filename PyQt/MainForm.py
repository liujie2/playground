# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu_E = QtWidgets.QMenu(self.menubar)
        self.menu_E.setObjectName("menu_E")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.fileOpenAction = QtWidgets.QAction(MainWindow)
        self.fileOpenAction.setObjectName("fileOpenAction")
        self.fileCreateAction = QtWidgets.QAction(MainWindow)
        self.fileCreateAction.setObjectName("fileCreateAction")
        self.fileCloseAction = QtWidgets.QAction(MainWindow)
        self.fileCloseAction.setObjectName("fileCloseAction")
        self.addWinAction = QtWidgets.QAction(MainWindow)
        self.addWinAction.setCheckable(True)
        self.addWinAction.setChecked(True)
        self.addWinAction.setEnabled(True)
        self.addWinAction.setObjectName("addWinAction")
        self.menu_F.addAction(self.fileOpenAction)
        self.menu_F.addAction(self.fileCreateAction)
        self.menu_F.addAction(self.fileCloseAction)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_F.setTitle(_translate("MainWindow", "文件（&F）"))
        self.menu_E.setTitle(_translate("MainWindow", "编辑（&E）"))
        self.fileOpenAction.setText(_translate("MainWindow", "打开"))
        self.fileOpenAction.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.fileCreateAction.setText(_translate("MainWindow", "新建"))
        self.fileCreateAction.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.fileCloseAction.setText(_translate("MainWindow", "关闭"))
        self.fileCloseAction.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.addWinAction.setText(_translate("MainWindow", "添加窗体"))