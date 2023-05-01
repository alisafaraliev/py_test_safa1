from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

app = QApplication([])

my_win = QWidget()
my_win.setWindowTitle('Моё первое приложение')
my_win.resize(400, 200)
my_win.show()

h_line =  QHBoxLayout()
hello = QLabel('Привет')

h_line.addWidget(hello, alignment = Qt.AlignCenter)
my_win.setLayout(h_line)

app.exec_()