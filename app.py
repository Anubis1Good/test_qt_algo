from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint
 
app = QApplication([])
 
# главное окно:
my_win = QWidget()
my_win.setWindowTitle('Лотерея')
my_win.move(100, 100)
my_win.resize(400, 200)


#виджеты окна: кнопка и надпись
button = QPushButton('Испытать удачу')
text = QLabel('Нажми, чтобы участвовать')
number1 = QLabel('?')
number2 = QLabel('?')


#расположение виджетов
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(number1, alignment = Qt.AlignCenter)
line.addWidget(number2, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
my_win.setLayout(line)
 
#функция, которая генерирует и показывает числа
def start_lottery():
    n1 = randint(0, 9)
    n2 = randint(0, 9)
    number1.setText(str(n1))
    number2.setText(str(n2))
    if n1 == n2:
        text.setText('Вы выиграли! Сыграйте снова')
    else:
        text.setText('Вы проиграли! Сыграйте снова')
 
#обработка нажатия на кнопку
button.clicked.connect(start_lottery)


my_win.show()
app.exec_()
