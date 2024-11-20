import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QComboBox

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Unit Converter')
        self.setGeometry(100, 100, 400, 200)

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText('Enter value to convert')

        self.convert_button = QPushButton('Convert', self)

        self.convert_button.clicked.connect(self.convert_value)

        self.from_unit = QComboBox()
        self.to_unit = QComboBox()

        units = ['Meters', 'Kilometers', 'Miles']
        self.from_unit.addItems(units)
        self.to_unit.addItems(units)

        layout = QVBoxLayout(self)
        layout.addWidget(self.from_unit)
        layout.addWidget(self.to_unit)
        layout.addWidget(self.input_field)
        layout.addWidget(self.convert_button)

        self.result = QLabel('Result will be shown here', self)
        layout.addWidget(self.result)

        self.setLayout(layout)

        self.apply_styles()

    def convert_value(self):
        try:
            input_text = self.input_field.text().strip()

            if not input_text:
                self.result.setText("Error: Input cannot be empty!")
                return

            input_number = float(input_text)

            from_unit = self.from_unit.currentText()
            to_unit = self.to_unit.currentText()

            conversion_rates = {
                'Kilometers': 1.0,
                'Meters': 1000,
                'Miles': 0.621371,
            }

            if from_unit == to_unit:
                result = input_number
            else:
                result = input_number * (conversion_rates[to_unit] / conversion_rates[from_unit])

            self.result.setText(f'Converted: {result} {to_unit}')

        except ValueError:
            self.result.setText('Error: please enter a valid number')

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
                image: url('assets/icons/down-arrow.png'); 
                width: 20px;
                height: 20px;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.show()
    sys.exit(app.exec_())