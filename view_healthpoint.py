import PySimpleGUI as sg
import markdown.markdown as md
from os import system

sg.theme('DarkAmber')
# Устанавливаем цвет внутри окна
layout = [
    [sg.Text("Cyberfest Tobolsk")]
]

# Создаем окно
window = sg.Window('Название окна', layout)
# Цикл для обработки "событий" и получения "значений" входных данных
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Отмена':
# если пользователь закрыл окно или нажал «Отмена»
        break
    print('Молодец, ты справился с вводом', values[0])

window.close()