from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui


# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# import sys

class AngledRect(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setMinimumSize(200, 200)

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setRenderHints(qp.Antialiasing)

        contents = self.contentsRect()
        # draw a line from the top left to the bottom right of the widget
        line = QtCore.QLineF(contents.topLeft(), contents.bottomRight())
        qp.drawLine(line)

        # save the current state of the painter
        qp.save()
        # translate to the center of the painting rectangle
        qp.translate(contents.center())
        # apply an inverted rotation, since the line angle is counterclockwise
        qp.rotate(-line.angle())

        # create a rectangle that is centered at the origin point
        rect = QtCore.QRect(-40, -10, 80, 20)
        qp.setPen(QtCore.Qt.white)
        qp.setBrush(QtCore.Qt.black)
        qp.drawRect(rect)
        qp.drawText(rect, QtCore.Qt.AlignCenter, '{:.05f}'.format(line.angle()))
        qp.restore()

        # ... other painting...
