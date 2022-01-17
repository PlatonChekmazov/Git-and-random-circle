import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 600, 400, 400)
        self.setWindowTitle('Рисование')
        self.btn = QPushButton('Рисовать', self)
        self.btn.move(100, 100)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)

    def draw_circle(self, qp):
        for i in range(randint(1, 10)):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            width = randint(1, 100)
            qp.drawEllipse(randint(1, 478), randint(1, 607), width, width)

    def paint(self):
        self.do_paint = True
        self.repaint()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())