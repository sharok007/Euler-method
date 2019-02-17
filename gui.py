# -*- coding: utf-8 -*-

#GUI built in QtDesigner

from PyQt5 import QtCore, QtWidgets

# class that creates a GUI
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(744, 486)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_equation = QtWidgets.QLabel(self.centralWidget)
        self.lbl_equation.setObjectName("lbl_equation")
        self.gridLayout.addWidget(self.lbl_equation, 0, 0, 1, 1)
        self.lbl_graphic = QtWidgets.QLabel(self.centralWidget)
        self.lbl_graphic.setObjectName("lbl_graphic")
        self.gridLayout.addWidget(self.lbl_graphic, 0, 3, 1, 1)
        self.list_equation = QtWidgets.QListWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_equation.sizePolicy().hasHeightForWidth())
        self.list_equation.setSizePolicy(sizePolicy)
        self.list_equation.setObjectName("list_equation")
        self.gridLayout.addWidget(self.list_equation, 1, 0, 1, 1)
        self.txt_solution = QtWidgets.QTextEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_solution.sizePolicy().hasHeightForWidth())
        self.txt_solution.setSizePolicy(sizePolicy)
        self.txt_solution.setObjectName("txt_solution")
        self.gridLayout.addWidget(self.txt_solution, 1, 2, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 1, 3, 1, 1)
        self.lbl_solution = QtWidgets.QLabel(self.centralWidget)
        self.lbl_solution.setObjectName("lbl_solution")
        self.gridLayout.addWidget(self.lbl_solution, 0, 2, 1, 1)
        self.btn_decide = QtWidgets.QPushButton(self.centralWidget)
        self.btn_decide.setObjectName("btn_decide")
        self.gridLayout.addWidget(self.btn_decide, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 744, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_equation.setText(_translate("MainWindow", "Equation"))
        self.lbl_graphic.setText(_translate("MainWindow", "Schedule"))
        self.lbl_solution.setText(_translate("MainWindow", "Solution"))
        self.btn_decide.setText(_translate("MainWindow", "Decide"))

