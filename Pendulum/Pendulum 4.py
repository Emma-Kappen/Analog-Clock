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
        # Updating the code every second
        pendulum_timer.timeout.connect(self.update)  # incorrect

        # setting start time of pendulum_timer to 1 second
        pendulum_timer.start(0)

        # setting window title
        self.setWindowTitle("Pendulum")

        # setting window geometry (size)
        self.setGeometry(500, 500, 300, 600)

        # setting background color to white
        self.setStyleSheet("background: white")

        # Creating pendulum chord + bob
        self.pPointer = QtGui.QPolygon([QPoint(6, 7),
                                        QPoint(-6, 7),
                                        QPoint(-3, -100),
                                        QPoint(-10, -120),
                                        QPoint(0, -140),
                                        QPoint(10, -120),
                                        QPoint(3, -100)])

        # color of pendulum chord + bob
        self.pColor = Qt.black

        # color of background
        self.bColor = Qt.black

        """
            # painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
            def paintEvent(self, event):
                painter = QPainter(self)
                painter.setPen(QPen(Qt.green, 8, Qt.SolidLine))
                painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
                painter.drawEllipse(40, 40, 400, 400)
            """

    # method for paint event
    def paintEvent(self, event):
        # getting minimum of width and height
        # so that clock remain square
        rec = min(self.width(), self.height())

        # defining the time period
        time_period = QTime.currentTime()

        # creating a painter object
        painter = QPainter(self)

        # method to draw the pendulum
        # argument : color rotation and which hand should be pointed
        def drawPointer(color, pointer, rotation):
            # setting brush
            painter.setBrush(QBrush(color))

            # saving painter
            painter.save()

            # rotating painter
            painter.rotate(rotation)  # * i

            # draw the polygon i.e pendulum
            painter.drawConvexPolygon(pointer)

            # restore the painter
            painter.restore()

        # tune up painter
        painter.setRenderHint(QPainter.Antialiasing)

        # translating the painter
        painter.translate(self.width() / 2, self.height() / 2)

        # scale the painter
        painter.scale(((rec - 100) / 200), ((rec - 100) / 200))

        # set current pen as no pen
        painter.setPen(QtCore.Qt.NoPen)

        # draw the hands and the clock case
        # drawPointer(self.o_pColor, 0, self.o_pPointer)
        # drawPointer(self.i_pColor, 0, self.i_pPointer)
        # drawPointer(self.bColor, (30 * (tik.hour() + tik.minute() / 60)), self.hPointer)
        # drawPointer(self.bColor, (6 * (tik.minute() + tik.second() / 60)), self.mPointer)
        # drawPointer(self.sColor, (6 * tik.second()), self.sPointer)
        drawPointer(self.pColor, self.pPointer, time_period.second())

        # drawing background
        painter.setPen(QPen(self.bColor))
        """
        # for loop
        for i in range(0, 60):

            # drawing background lines
            if (i % 5) == 0:
                painter.drawLine(87, 0, 97, 0)
        
            # rotating the painter
            painter.rotate(6)
        """
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
