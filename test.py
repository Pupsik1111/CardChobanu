#начни тут создавать приложение с умными заметками
import json
from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,QRadioButton,QGroupBox, QButtonGroup, QLineEdit,QListWidget,QTextEdit



app = QApplication([])


my_win = QWidget()
my_win.setWindowTitle('Умные Заметки')
my_win.move(100, 100)
my_win.resize(800,800)



big= QTextEdit('fcgh')
txt=QLabel('Список заметок')
listoc=QListWidget()
nipon=QPushButton('Создать заметку')
nopin=QPushButton('Удалить заметку')
cnop=QPushButton('Сохранить заметку')
txt2=QLabel('Сптсок тегов')
listoc2=QListWidget()
nipon2=QPushButton('Добавит к заметке')
nopin2=QPushButton('Открепить от заметки')
cnop2=QPushButton('Искать заметки по тегу')
line = QLineEdit('')
line.setPlaceholderText('Введите тег...')



main_allaut=QHBoxLayout()


vtoroy=QVBoxLayout()
tretyi=QVBoxLayout()
chetire=QHBoxLayout()
pyatiy=QHBoxLayout()

main_allaut.addLayout(vtoroy)
main_allaut.addLayout(tretyi)
tretyi.addLayout(chetire)
tretyi.addLayout(pyatiy)

main_allaut.addWidget(my_win)
vtoroy.addWidget(big)
tretyi.addWidget(txt)
tretyi.addWidget(listoc)
chetire.addWidget(nipon)
chetire.addWidget(nopin)
tretyi.addWidget(cnop)
tretyi.addWidget(txt2)
tretyi.addWidget(listoc2)
pyatiy.addWidget(nipon2)
pyatiy.addWidget(nopin2)
tretyi.addWidget(cnop2)
tretyi.addWidget(line)


my_win.show()
app.exec_()