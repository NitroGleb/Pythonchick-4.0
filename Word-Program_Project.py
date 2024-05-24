from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QListWidget,QInputDialog,QLabel,QPushButton,QApplication,QVBoxLayout,QHBoxLayout,QWidget,QLineEdit,QTextEdit)
import json

app = QApplication([])

notes = QTextEdit()
field_text = QTextEdit()

text = QLabel('Список заметок')
list_notes = QListWidget()
#txtt = QHBoxLayout()
btn = QPushButton('Удалить заметку')
btn2 = QPushButton('Сохранить заметку')
btn3 = QPushButton('Создать заметку')
list_tages = QListWidget()
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
main_h1.addWidget(notes,stretch=7)
main_h1.addLayout(v2,stretch=5)

v1.addWidget(text)
v2.addWidget(list_notes)
v2.addWidget(list_notes)
v2.addLayout(h1)
h1.addWidget(btn)
h1.addWidget(btn2)
v2.addWidget(btn3)
v2.addWidget(list_tages)
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
main_w1.addWidget(list_notes,stretch=8)
main_w1.addLayout(v2,stretch=6)


def add_check():
    note_name, ok = QInputDialog.getText(teger,'Создать заметку', 'Название заметки:')
    if ok and note_name != "":
        notes[note_name] = {"текст":"", "теги": []}
        list_notes.addItem(note_name)
        list_tages.addItems(notes[note_name]["теги"])

def delete_check():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tages.clear()
        notes.clear()
        list_notes.addItems(notes)
        with open("notes.json", "w", encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('Заметка для удаления не выбрана!')

def save_check():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['текст'] = field_text.toPlainText()
        with open("notes.json", "w", encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('Заметка для сохранения не выбрана!')

def checker():
    key = list_notes.selectedItems()[0].text()
    print(key)
    notes.setText(notes[key]["текст"])
    list_tages.clear()
    list_tages.addItems(notes[key]["теги"])

def add_teg():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]["теги"]:
            notes[key]['текст'].append(tag)
            list_tages.addItem(tag)
            field_tag.clear()
        with open("notes_file.json", "w", encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('Заметка для сохранения не выбрана!')

def delete_teg():
    if list_notes.currentItem() and list_tages.currentItem():
        note_name = list_notes.currentItem().text()
        tag_name = list_tages.currentItem().text()
        notes[note_name]['tags'].remove(tag_name)

        cur_row = list_tages.currentRow()
        list_tages.takeItem(cur_row)
        with open("notes.json", "w", encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)

def find_teg():
    print(teger.text())
    tag = field_tag.text()
    if teger.text() == 'Искать заметку по тегу' and tag:
        print(tag)
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]['теги']:
                notes_filtered[note] = notes[note]
        teger.setText('Сбросить поиск')
        list_notes.clear()
        list_tages.clear()
        list_notes.addItems(notes_filtered)
        print(teger.text())
    elif teger.text() == 'Сбросить поиск':
        field_tag.clear()
        list_notes.clear()
        list_tages.clear()
        list_notes.addItems(notes)
        teger.setText('Искать заметки по тегу')
        print(teger.text())
    else:
        pass

try:
    with open("notes.json", "r", encoding='utf-8') as file:
        notes = json.load(file)
    list_notes.addItems(notes)
except FileNotFoundError:
    notes = {}

btn.clicked.connect(delete_check)
btn2.clicked.connect(save_check)
btn3.clicked.connect(add_check)
btn4.clicked.connect(add_teg)
btn5.clicked.connect(delete_teg)
btn6.clicked.connect(find_teg)

window.show()
app.exec()