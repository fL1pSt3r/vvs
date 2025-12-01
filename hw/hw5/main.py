import sys
import random
import string
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QHBoxLayout,
    QCheckBox,
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Генератор паролей")
        self.setGeometry(100, 100, 250, 150)

        layout = QVBoxLayout()

        self.label = QLabel("Пароль:")
        layout.addWidget(self.label)

        self.password = QLineEdit("")
        layout.addWidget(self.password)

        self.button = QPushButton("Сгенерировать пароль")
        self.button.clicked.connect(self.generate_password)
        layout.addWidget(self.button)

        length_layout = QHBoxLayout()
        self.length_label = QLabel("Длина:")
        length_layout.addWidget(self.length_label)

        self.length = QLineEdit("12")
        self.length.setFixedWidth(40)
        length_layout.addWidget(self.length)
        layout.addLayout(length_layout)

        self.specials_checkbox = QCheckBox("Спецсимволы")
        self.specials_checkbox.setChecked(True)
        layout.addWidget(self.specials_checkbox)

        self.setLayout(layout)

    def generate_password(self):
        try:
            length = int(self.length.text())
            if length < 1:
                raise
        except:
            self.password.setText("Введите натуральное число")
            return

        chars = string.ascii_letters + string.digits

        if self.specials_checkbox.isChecked():
            chars += string.punctuation

        password = "".join(random.choice(chars) for _ in range(length))
        self.password.setText(password)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
