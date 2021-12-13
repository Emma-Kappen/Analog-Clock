import sys, random
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QFrame, QGridLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QEvent, QMimeData
from PyQt5.QtGui import QDrag
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasAgg as FigureCanvas


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multiple Graphs in a single window")
        self.setMinimumSize(1400, 1400)
        self.setAcceptDrops(True)

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # graph window container
        self.graphContainer = QWidget()
        self.gridLayout = QGridLayout(self.graphContainer)

        self.scrollArea.setWidget(self.graphContainer)
        self.layout.addWidget(self.scrollArea)

    def createGraphs(self):
        tracker = 0

        for c in range(3):
            for r in range(3):
                frame = QFrame()
                frame.setStyleSheet("background-color: white;")
                frame.setFrameStyle(QFrame.Panel | QFrame.Raised)

                frameContainer = QVBoxLayout()

                chartData = [random.random() for i in range(9)]
                tracker += 1

                # create matplotlib graph
                figure = Figure()
                canvas = FigureCanvas()  # pyqt5 widget
                ax = figure.add_subplot()
                ax.plot(chartData, "-")
                figure.suptitle("Chrat #{0}".format(tracker))
                canvas.draw()

                # TODO: Drag and Drop feature
                frameContainer.addWidget(canvas)

                box = QVBoxLayout()
                box.addWidget(frame)

                self.gridLayout.addLayout(box, r, c)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("App is closing")
