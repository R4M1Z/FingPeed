# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
import time,os,sys
from threading import Thread

class Ui_MainWindow(object):
    file = open("words.txt")
    words = file.readlines()
    trueWrited = 0
    wrongWrited = -1
    delay = 60
    def quit(self):
        app.quit()
    def timer(self):
        while (Ui_MainWindow.delay>0):
            Ui_MainWindow.delay-=1
            time.sleep(1)
            _translate = QtCore.QCoreApplication.translate
            self.secs.setText(_translate("MainWindow", "Vaxt : "+str(Ui_MainWindow.delay)))
        if(Ui_MainWindow.delay==0):
            self.writedWord.returnPressed.connect(self.quit)
            self.writedWord.setText("")
            self.writedWord.setGeometry(0,0,0,0)
            self.newWord.setText("")
            font=QtGui.QFont()
            font.setPointSize(17)
            self.newWord.resize(580,350)
            self.newWord.setFont(font)
            self.newWord.setText("Time over. Correct words = "+str(self.trueWrited)+". Press ENTER to exit")
            self.secs.setText("Time over")
            self.secs.setStyleSheet("color:red;")
    def clear(self):
        _translate = QtCore.QCoreApplication.translate
        length=len(self.newWord.text())
        if(Ui_MainWindow.delay>0):
            if (self.writedWord.text()==self.newWord.text()[:length-1]):
                Ui_MainWindow.trueWrited +=1
            else:
                Ui_MainWindow.wrongWrited+=1
        else:
            pass
        self.writedWord.setText("")
        self.newWord.setText(_translate("MainWindow", Ui_MainWindow.words[randint(0,2999)]))
        self.TrueWords.setText(_translate("MainWindow", "Correct : "+str(Ui_MainWindow.trueWrited)))
        self.WrongWords.setText(_translate("MainWindow", "Wrong : "+str(Ui_MainWindow.wrongWrited)))
        self.WrongWords.setStyleSheet("color:red;")
    def start(self):
        th1=Thread(target=self.timer)
        th2=Thread(target=self.clear)
        th3=Thread(target=self.quit)
        if (Ui_MainWindow.delay==60):
            th1.start()
        th2.start()
        if(Ui_MainWindow.delay==0):
            th3.start()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 454)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(True)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background:#384B4F; color:#f0f0f0")
        self.centralwidget.setObjectName("centralwidget")
        self.writedWord = QtWidgets.QLineEdit(self.centralwidget)
        self.writedWord.setGeometry(QtCore.QRect(90, 220, 391, 61))
        self.writedWord.setText("")
        fontww = QtGui.QFont()
        fontww.setPointSize(17)
        self.writedWord.setFont(fontww)
        self.writedWord.setFrame(False)
        self.writedWord.setAlignment(QtCore.Qt.AlignCenter)
        self.writedWord.setObjectName("writedWord")
        self.writedWord.returnPressed.connect(self.start)
        self.newWord = QtWidgets.QLabel(self.centralwidget)
        self.newWord.setGeometry(QtCore.QRect(30, 30, 531, 141))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.newWord.setFont(font)
        self.newWord.setAlignment(QtCore.Qt.AlignCenter)
        self.newWord.setObjectName("newWord")

        self.TrueWords = QtWidgets.QLabel(self.centralwidget)
        self.TrueWords.setGeometry(QtCore.QRect(450, 10, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.TrueWords.setFont(font)
        self.TrueWords.setAlignment(QtCore.Qt.AlignCenter)
        self.TrueWords.setObjectName("TrueWords")

        self.WrongWords = QtWidgets.QLabel(self.centralwidget)
        self.WrongWords.setGeometry(QtCore.QRect(450, 40, 121, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.WrongWords.setFont(font)
        self.WrongWords.setAlignment(QtCore.Qt.AlignCenter)
        self.WrongWords.setObjectName("WrongWords")

        self.secs = QtWidgets.QLabel(self.centralwidget)
        self.secs.setGeometry(QtCore.QRect(10, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.secs.setFont(font)
        self.secs.setAlignment(QtCore.Qt.AlignCenter)
        self.secs.setObjectName("secs")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 603, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Test Your Finger Speed", "FingPeed"))
        MainWindow.setWindowIcon(QtGui.QIcon("icon.svg"))
        self.newWord.setText(_translate("MainWindow", "Press ENTER to begin."))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
