# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

def function():
    print("cc")

    
stav = "připraven"

class Ui_AMSG(object):
    def setupUi(self, AMSG):
        AMSG.setObjectName("AMSG")
        AMSG.resize(530, 426)
        self.centralwidget = QtWidgets.QWidget(AMSG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(530, 426))
        self.centralwidget.setMaximumSize(QtCore.QSize(531, 427))
        self.centralwidget.setObjectName("centralwidget")


        
        self.delicicara = QtWidgets.QFrame(self.centralwidget)
        self.delicicara.setGeometry(QtCore.QRect(100, 0, 20, 421))
        self.delicicara.setFrameShape(QtWidgets.QFrame.VLine)
        self.delicicara.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.delicicara.setObjectName("delicicara")
        self.greeting = QtWidgets.QLabel(self.centralwidget)
        self.greeting.setGeometry(QtCore.QRect(246, 20, 81, 41))

        
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.greeting.setFont(font)
        self.greeting.setTextFormat(QtCore.Qt.AutoText)
        self.greeting.setAlignment(QtCore.Qt.AlignCenter)
        self.greeting.setObjectName("greeting")

        
        self.generate = QtWidgets.QPushButton(self.centralwidget)
        self.generate.setGeometry(QtCore.QRect(140, 220, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.generate.setFont(font)
        self.generate.setObjectName("generate")

        
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(320, 220, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.play.setFont(font)
        self.play.setObjectName("play")
        self.play.clicked.connect(function)
        
        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(440, 390, 75, 23))
        self.quit.setObjectName("quit")
    

        
        self.repete = QtWidgets.QSpinBox(self.centralwidget)
        self.repete.setGeometry(QtCore.QRect(330, 130, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.repete.setFont(font)
        self.repete.setMinimum(1)
        self.repete.setProperty("value", 10)
        self.repete.setObjectName("repete")

        
        self.repetelab = QtWidgets.QLabel(self.centralwidget)
        self.repetelab.setGeometry(QtCore.QRect(140, 130, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.repetelab.setFont(font)
        self.repetelab.setObjectName("repetelab")

        
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(20, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.help.setFont(font)
        self.help.setObjectName("help")

        
        self.about = QtWidgets.QPushButton(self.centralwidget)
        self.about.setGeometry(QtCore.QRect(20, 60, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.about.setFont(font)
        self.about.setObjectName("about")

        
        self.situation = QtWidgets.QLabel(self.centralwidget)
        self.situation.setGeometry(QtCore.QRect(140, 310, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.situation.setFont(font)
        self.situation.setObjectName("situation")

        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 321, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        AMSG.setCentralWidget(self.centralwidget)

        self.retranslateUi(AMSG)
        QtCore.QMetaObject.connectSlotsByName(AMSG)

    def retranslateUi(self, AMSG):
        _translate = QtCore.QCoreApplication.translate
        
        AMSG.setWindowTitle(_translate("AMSG", "AMSG - Automatic Music Score Generator"))
        AMSG.setWhatsThis(_translate("AMSG", "AMSG"))
        AMSG.setAccessibleName(_translate("AMSG", "AMSG"))
        
        self.greeting.setText(_translate("AMSG", "Vítej!"))
        
        self.generate.setText(_translate("AMSG", "GENEROVAT"))
        
        self.play.setText(_translate("AMSG", "PŘEHRÁT"))
        
        self.quit.setText(_translate("AMSG", "ukončit"))
        
        self.repetelab.setText(_translate("AMSG", "Počet opakování:"))
        
        self.help.setText(_translate("AMSG", "Nápověda"))
        
        self.about.setText(_translate("AMSG", "O programu"))
        
        self.situation.setText(_translate("AMSG", "Aktuální stav:"))
        
        self.label.setText(_translate("AMSG", str(stav)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AMSG = QtWidgets.QMainWindow()
    ui = Ui_AMSG()
    ui.setupUi(AMSG)
    AMSG.show()
    sys.exit(app.exec_())