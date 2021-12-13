
"""
# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Pendulum(QMainWindow):

    # constructor
    def __init__(self):
        super().__init__()

        # creating a timer object
        pendulum_timer = QTimer(self)

        # Adding action to the pendulum_timer
        # Updating the code every two seconds
        pendulum_timer.timeout.connect(self.update)  # incorrect

        # setting start time of pendulum_timer to 0 seconds
        pendulum_timer.start(0)

        # setting window title
        self.setWindowTitle("Pendulum")

        # setting window geometry (size)
        self.setGeometry(300, 600, 300, 600)

        # setting background color to white
        self.setStyleSheet("background: white")

        # Creating pendulum chord
        self.pPointer = QtGui.QPolygon([QPoint(6, 7),
                                        QPoint(-6, 7),
                                        QPoint(0, -100)])

        # color of pendulum chord
        self.pColor = Qt.black

        # Creating pendulum bob
        self.bPointer = QtGui.QPolygon

        # painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        def paintEvent(self, event):
            painter = QPainter(self)
            painter.setPen(QPen(Qt.green, 8, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
            painter.drawEllipse(40, 40, 400, 400)

        # method for paint event

    def paintEvent(self, event):
        # getting minimum of width and height
        # so that clock remain square
        rec = min(self.width(), self.height())

        # defining the time period
        time_period = 2000

        # creating a painter object
        painter = QPainter(self)

        # method to draw the hands
        # argument : color rotation and which hand should be pointed
        def drawPointer(color, alpha, pointer):
            # setting brush
            painter.setBrush(QBrush(color))

            # saving painter
            painter.save()

            # rotating painter
            painter.rotate(rotation)

            # draw the polygon i.e hand
            painter.drawConvexPolygon(pointer)

            # restore the painter
            painter.restore()

        # tune up painter
        painter.setRenderHint(QPainter.Antialiasing)

        # translating the painter
        painter.translate(self.width() / 2, self.height() / 2)

        # scale the painter
        painter.scale(rec / 200, rec / 200)

        # set current pen as no pen
        painter.setPen(QtCore.Qt.NoPen)

        # draw each hand
        drawPointer(self.sColor, (6 * time_period.second()), self.sPointer)

        # drawing background
        painter.setPen(QPen(self.bColor))


# Driver code
if __name__ == '__main__':
    app = QApplication(sys.argv)

# creating a clock object
win = Pendulum()

# show
win.show()

exit(app.exec_())

"""

# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


# creating a pendulum class
class Pendulum(QMainWindow):

    # constructor
    def __init__(self):
        super().__init__()

        # creating a timer object
        timer = QTimer(self)

        # adding action to the timer
        # update the whole code
        timer.timeout.connect(self.update)  # change here

        # setting start time of timer i.e 0 seconds
        timer.start(1000)

        # setting window title
        self.setWindowTitle('Pendulum')

        # setting window geometry
        self.setGeometry(300, 300, 800, 800)

        # setting background color to the window
        self.setStyleSheet("background : white;")

        # creating pendulum chord
        self.pc_Pointer = QtGui.QPolygon([QPoint(6, 7),
                                          QPoint(-6, 7),
                                          QPoint(0, -100)])

        """
        # creating minute hand
        self.mPointer = QPolygon([QPoint(6, 7),
                                  QPoint(-6, 7),
                                  QPoint(0, -50)])
        
        """
        # creating pendulum bob
        self.pb_Pointer = QtGui.QPolygon([QPoint(200, 200),  # Figure it out-Not Done
                                          QPoint(500, 500),
                                          QPoint(500, 500),
                                          QPoint(200, 200)])

        # creating pendulum box
        self.bPointer = QtGui.QPolygon([QPoint(100, 100),
                                        QPoint(-100, 100),
                                        QPoint(0, -100)])

        # colors
        # color for pendulum chord
        self.pc_Color = Qt.black

        # color for pendulum bob
        self.pb_Color = Qt.red

        # color for pendulum box
        self.bColor = Qt.red

        # method for paint event

    def paintEvent(self, event):
        # getting minimum of width and height
        # so that clock remain square
        rec = min(self.width(), self.height())

        # getting current time
        tik = QTime.currentTime()

        # creating a painter object
        painter = QPainter(self)

        # method to draw the hands
        # argument : color rotation and which hand should be pointed
        def drawPointer(color, swing, pointer):
            # setting brush
            painter.setBrush(QBrush(color))

            # saving painter
            painter.save()

            # rotating painter
            painter.rotate(swing)

            # draw the polygon i.e hand
            painter.drawConvexPolygon(pointer)

            # restore the painter
            painter.restore()

            # tune up painter
            painter.setRenderHint(QPainter.Antialiasing)

            # translating the painter
            painter.translate(self.width() / 2, self.height() / 2)

            # scale the painter
            painter.scale(rec / 200, rec / 200)

            # set current pen as no pen
            painter.setPen(QtCore.Qt.NoPen)

            # draw the chord and bob
            drawPointer(self.pc_Color, (30 * (tik.minute() / 60)), self.pc_Pointer)
            drawPointer(self.pb_Color, (6 * (tik.second() / 60)), self.pb_Pointer)
            drawPointer(self.bColor, 0, self.bPointer)

            # drawing background
            painter.setPen(QPen(self.bColor))

            # ending the painter
            painter.end()


# Driver code
if __name__ == '__main__':
    app = QApplication(sys.argv)

# creating a clock object
win = Pendulum()

# show
win.show()

exit(app.exec_())
