import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel

''' 1 шаг Создание основного окна:
импорты - sys для завершения приложения
            QApplication - для запуска любого приложения PyQt
            QWidget - для создания любого окна
Создаем класс основного окна
Пишем конструктор, наследуемся от родительского класса QWidget
Задаем название, задаем расположение.

    2 шаг Создание базового интерфейса
Добавление текстового поля, кнопки, создание вертикального макета
Про setlayout:
Без вызова self.setLayout(layout) PyQt не знает, как именно размещать элементы в окне. 
Они либо не будут видны, либо появятся в хаотичном порядке.
После установки макета PyQt:
Рассчитывает размеры и позиции всех элементов на основе логики макета.
Динамически перестраивает элементы, если пользователь изменяет размер окна.
По сути, self.setLayout(layout) связывает компоновку (layout) с текущим виджетом, завершая процесс настройки расположения.

    3 шаг Логика нажатия кнопки
Кнопка будет считывать введённое значение из текстового поля 
и отображать преобразованный результат (пока просто в консоли, чтобы проверить работу).
    
Связать кнопку с функцией: для этого используется метод clicked.connect(). 
Он связывает кнопку с определённой функцией, которая будет выполняться при нажатии.

Создать функцию для обработки события: эта функция будет считывать текст из текстового поля и выводить его в консоль.

    4 шаг Вывод результата
Добавить метку для вывода результата: используем QLabel, который будет обновляться при нажатии кнопки.
Обновить метод convert_value: вместо вывода текста в консоль будем менять текст метки.
    
'''
class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Unit Converter')
        self.setGeometry(100, 100, 400, 200)

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText('Enter value to convert') # leave a hint for a user
        self.convert_button = QPushButton('Convert', self)

        self.convert_button.clicked.connect(self.convert_value)

        layout = QVBoxLayout(self) # create layout, adding elements to layout
        layout.addWidget(self.input_field)
        layout.addWidget(self.convert_button)

        self.result = QLabel('Result will be shown here', self) # create a label and add it to layout to show the result
        layout.addWidget(self.result)

        self.setLayout(layout) # set layout from above

    def convert_value(self):
        input_text = self.input_field.text() # get the text from the field
        converted_text = f'Converted: {input_text}' # just add information to user's input, add two strings
        self.result.setText(converted_text) # update label text




'''
app = QApplication(sys.argv) — создает объект приложения, который управляет главным циклом событий.
window = ConverterApp() — создаем экземпляр нашего окна.
window.show() — показываем окно.
sys.exit(app.exec_()) — запускаем главный цикл событий.
'''
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.show()
    sys.exit(app.exec_())