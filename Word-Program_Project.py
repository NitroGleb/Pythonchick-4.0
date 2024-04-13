from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QListWidget,QLabel,QPushButton,QApplication,QVBoxLayout,QHBoxLayout,QWidget,QLineEdit,QTextEdit)
import json

app = QApplication([])

text_field = QTextEdit()
text_field2 = QTextEdit()

text = QLabel('Список заметок')
textiner = QListWidget()
txtt = QHBoxLayout()
btn = QPushButton('Удалить заметку')
btn2 = QPushButton('Сохранить заметку')
btn3 = QPushButton('Создать заметку')
textiner2 = QListWidget()
btn4 = QPushButton('Добавить к заметке')
btn5 = QPushButton('Открепить от заметки')
btn6 = QPushButton('Искать заметку по тегу')
teger = QLineEdit()
teger.setPlaceholderText('Введите тег...')

v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()

main_h1 = QHBoxLayout()
main_h1.addWidget(text_field,stretch=7)
main_h1.addLayout(v2,stretch=5)

v1.addWidget(text)
v2.addWidget(textiner)
v2.addLayout(h1)
h1.addWidget(btn)
h1.addWidget(btn2)
v2.addWidget(btn3)
v2.addWidget(textiner2)
v2.addWidget(teger)
v2.addLayout(h2)
h2.addWidget(btn4)
h2.addWidget(btn5)
v2.addWidget(btn6)

window = QWidget()
window.resize(900,600)
window.setLayout(main_h1)

list_tages = QListWidget()

field_tag = QLineEdit()

main_w1 = QVBoxLayout()
main_w1.addWidget(text_field2,stretch=8)
main_w1.addLayout(v2,stretch=6)

def delete_check():
    pass

def save_check():
    pass

def checker():
    pass

def add_teg():
    pass

def delete_teg():
    pass

def find_teg():
    pass

btn.clicked.connect(delete_check)
btn2.clicked.connect(save_check)
btn3.clicked.connect(checker)
btn4.clicked.connect(add_teg)
btn5.clicked.connect(delete_teg)
btn6.clicked.connect(find_teg)

window.show()
app.exec()