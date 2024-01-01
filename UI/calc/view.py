from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt

class View(QMainWindow):

    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("My Calculator")
        self.setFixedSize(240, 280)

        self.__central_widget = QWidget(self)
        self.setCentralWidget(self.__central_widget)

        self.__general_layout = QVBoxLayout()
        self.__central_widget.setLayout(self.__general_layout)

        self.__create_display()
        self.__create_buttons()

    def __create_display(self):
        self.__display = QLineEdit()
        self.__display.setFixedHeight(35)
        self.__display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.__display.setReadOnly(True)
        self.__general_layout.addWidget(self.__display)

    def __create_buttons(self):
        buttons_dict = {'7': (0, 0),
            '8': (0, 1),
            '9': (0, 2),
            '/': (0, 3),
            'C': (0, 4),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '*': (1, 3),
            '(': (1, 4),
            '1': (2, 0),
            '2': (2, 1),
            '3': (2, 2),
            '-': (2, 3),
            ')': (2, 4),
            '0': (3, 0),
            '00': (3, 1),
            '.': (3, 2),
            '+': (3, 3),
            '=': (3, 4),
            }

        self.__buttons_layout = QGridLayout()
        self.__buttons = {}

        for text, pos in buttons_dict.items():
            self.__buttons[text] = QPushButton(text)
            self.__buttons[text].setFixedSize(40,40)
            self.__buttons_layout.addWidget(self.__buttons[text], pos[0], pos[1])

        self.__general_layout.addLayout(self.__buttons_layout)

    def get_buttons(self):
        return self.__buttons

    def get_display_text(self):
        return self.__display.text()

    def set_display_text(self, text):
        self.__display.setText(text)

    def clear_display(self):
        self.__display.setText("")