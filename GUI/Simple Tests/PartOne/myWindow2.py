from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,700,400)
        self.setWindowTitle("cvTracker")
        self.setWindowIcon(QIcon('Graphical_elements/LogoRezisedto256x256.png'))
        self.setWindowOpacity(0.5)


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())