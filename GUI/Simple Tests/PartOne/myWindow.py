from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

app =QApplication(sys.argv)

window = QMainWindow()
window.menuBar().addMenu("File")
window.menuBar().addMenu("Edit")
window.menuBar().addMenu("View")
window.menuBar().addMenu("Window")
window.menuBar().addMenu("Help")



window.show()

sys.exit(app.exec())