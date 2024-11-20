import sys
from PyQt5.QtWidgets import QApplication, QWidget

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Unit Converter')
        self.setGeometry(100, 100, 400, 200)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.show()
    sys.exit(app.exec_())