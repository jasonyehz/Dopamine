import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QProgressBar, QMainWindow
from PyQt6.QtCore import QSize, Qt

# Subclass QMainWindow to customize the main window

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Dopamine")
		button = QPushButton("Press Me!")


		self.setFixedSize(400, 300)
		self.setCentralWidget(button)

app = QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec()
