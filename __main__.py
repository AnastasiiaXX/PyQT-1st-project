import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QComboBox
from PyQt5.QtCore import Qt
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
    
    5 шаг Добавление логики конвертации
Начинаем с конвертации чисел.
Добавить проверку ввода, чтобы работать только с числами.
Реализовать простую логику конвертации (например, умножение числа на 1000 для перевода километров в метры).
Если пользователь вводит нечисловое значение, выводить ошибку в метке результата.

    Шаг 6: Добавление выбора единиц измерения
Теперь мы добавим два выпадающих списка (QComboBox) для выбора исходной и целевой единиц измерения.
Создать выпадающие списки:
Один для выбора исходной единицы.
Второй для выбора целевой единицы.

Добавить их в компоновку:
Расположим выпадающие списки над полем ввода и кнопкой.
Заполнить выпадающие списки вариантами: "kilometers", "meters", "miles".

    Шаг 7: Реализация логики преобразования
Создадим словарь с коэффициентами преобразования: для преобразования из километров в метры, мили и так далее.

Получим выбранные пользователем единицы:будем получать выбранные значения из двух выпадающих списков (исходную и целевую единицу).

Используем коэффициенты для преобразования:
Если выбранные единицы одинаковые (например, километры в километры), просто вернем исходное значение.
Если они разные, применим коэффициент из словаря.

Обновим результат: После преобразования обновим текст на метке с результатом.
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

        self.from_unit = QComboBox()  # two combo boxes "from _unit_ to _unit_"
        self.to_unit = QComboBox()

        units = ['meters', 'kilometers', 'miles'] # add list of units to combobox
        self.from_unit.addItems(units)
        self.to_unit.addItems(units)

        layout = QVBoxLayout(self) # create layout, adding elements to layout
        layout.addWidget(self.from_unit)
        layout.addWidget(self.to_unit)
        layout.addWidget(self.input_field)
        layout.addWidget(self.convert_button)

        self.result = QLabel('Result will be shown here', self) # create a label and add it to layout to show the result
        layout.addWidget(self.result)


        self.setLayout(layout) # set layout from above

        self.apply_styles()

    def convert_value(self):
        try:
            input_text = self.input_field.text().strip()  # get the text from the field

            if not input_text:
                self.result.setText("Error: Input cannot be empty!")
                return

            input_number = float(input_text) # convert string to float type

            from_unit = self.from_unit.currentText() # get the user's choice from combobox
            to_unit = self.to_unit.currentText()

            conversion_rates = { # a dictionary with coefficients
                'kilometers': 1.0,
                'meters': 1000,
                'miles': 0.621371,
            }

            if from_unit == to_unit: # if the same measurements, return user's input
                result = input_number
            else: #conversion_rates[to_unit] = to_unit is a string from to_unit = self.to_unit.currentText() that corresponds with the same key in the dict
                result = input_number * (conversion_rates[to_unit] / conversion_rates[from_unit])
            self.result.setText(f'Converted: {result} {to_unit}') # update label based on conversion
                                                            # result is the result of calculation
        except ValueError:                                   # {to_unit} a key in the dict that a user chose
            self.result.setText('Error: please enter a valid number') # if not a num, show an error text

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
            }
            QLineEdit {
                padding: 5px;
                font-size: 16px;
                border: 1px solid #ccc;
                border-radius: 5px;
                margin: 10px 0;
            }
            QLabel {
                font-size: 18px;
                color: #333;
                margin: 10px 0;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                padding: 10px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QComboBox {
                padding: 5px;
                font-size: 16px;
                border: 1px solid #ccc;
                border-radius: 5px;
                margin: 10px 0;
                min-width: 150px;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left: 1px solid #ccc;
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
            }
            QComboBox::down-arrow {
                image: url('./down-arrow.png'); 
                width: 20px;
                height: 20px;
            }
        """)


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