
from PyQt5 import QtGui,QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton,QMainWindow,QLabel,QVBoxLayout,QWidget,QMessageBox,QPushButton,QLineEdit
from PyQt5.QtGui import QIcon,QPainter,QBrush, QPainterPathStroker,QPen,QPixmap,QFont, QWindow
from PyQt5.QtCore import QSize,Qt,QTimer,QTime
import sys
import pyttsx3


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "databucket"
        self.top = 100
        self.left = 100
        self.width = 555
        self.height = 11997
        self.setWindowIcon(QtGui.QIcon("tt.png"))
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("r.png"))
        self.label.setGeometry(0,0,555,1197)
        self.InitWindow()

    def InitWindow(self):
        self.label2 = QLabel (self)
        self.label2.setPixmap(QPixmap("E.png"))
        self.label2.setGeometry(110,200,346,117)
        self.linedit = QLineEdit(self)
        self.linedit.move (90,400)
        self.linedit.move (380,60)
        self.button = QPushButton("",self)
        self.button.setIcon(QIcon("speak.png"))
        size = QSize(185,184)
        self.button.setIconSize(size)
        self.button.setStyleSheet("border: 0pxsolid white; border-radius:55px;")
        self.button.setGeometry(8,700,550,450)
        self.button.clicked.connect(self.onClick)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()


    def onClick(self):
        textValue = self.linedit.text()
        QMessageBox.question (self,"LineEdit","You Typed"+ textValue , QMessageBox.Ok)
        print(textValue)
        engine = pyttsx3.init()
        engine.say(textValue)
        engine.runAndWait()
        print("done")

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
                

