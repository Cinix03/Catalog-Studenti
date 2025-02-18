import sys
from PyQt6.QtWidgets import QSizePolicy, QListWidget
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QLabel, QLineEdit, QHBoxLayout


class AdminPage(QWidget):
    def __init__(self, serviceStud, serviceDisc, serviceNote):
        super().__init__()
        self.__serviceStud = serviceStud
        self.__serviceDisc = serviceDisc
        self.__serviceNote = serviceNote
        self.setWindowTitle("Admin Page")
        self.setFixedSize(600, 300)  # Dimensiune fixă 600x300

        self.label_search = QLabel("Cauta dupa nume: ",self)
        self.text_input = QLineEdit(self)
        self.text_input.setFixedWidth(135)
        self.stud_list = QListWidget(self)
        self.button_search = QPushButton("Search", self)
        self.button_search.setFixedSize(100, 20)
        layoutSecundar = QVBoxLayout()
        layoutSecundar.setSpacing(10)
        layoutSecundar.setContentsMargins(0, 0, 0, 0)

        container = QWidget()
        container.setLayout(layoutSecundar)

        layoutSecundar.addWidget(self.label_search)
        layoutSecundar.addWidget(self.text_input)
        layoutSecundar.addWidget(self.button_search)

        layout = QHBoxLayout()
        layout.addWidget(container, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.stud_list, alignment=Qt.AlignmentFlag.AlignCenter)
        self.stud_list.setFixedSize(QSize(200, 250))
        self.setLayout(layout)
        self.__populeazaLista()


    def __populeazaLista(self):
        studenti = self.__serviceStud.get_all_students()
        for stud in studenti:
            self.stud_list.addItem(stud)