from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys



class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("jdsa")

        vbox = QVBoxLayout(self)

        self.webEngineView = QWebEngineView()
        vbox.addWidget(self.webEngineView)
        vbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(vbox)

        self.webEngineView.setUrl(QUrl(""))
        self.show()

    def closeEvent(self, event):
        print("hej")
        event.accept()



def run_app():
    main = QApplication(sys.argv)
    window = Window()
    sys.exit(main.exec_())

if __name__ == "__main__":
    run_app()
