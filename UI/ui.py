import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QPushButton

def say_hi():
    if message.text():
        message.setText("")
    else:
        message.setText("Hello World!!!")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and slots')

layout = QVBoxLayout()

button = QPushButton('Say Hi!!!')
button.clicked.connect(say_hi)

layout.addWidget(button)

message = QLabel('')
layout.addWidget(message)

window.setLayout(layout)
window.show()

sys.exit(app.exec())