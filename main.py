import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                                 QLabel, QTextEdit, QLineEdit, QPushButton)


class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Colors
        first_color = "#677DB7"  # Blue
        second_color = "#A8BA9A"  # Light Green
        third_color = "#0D5D56"  # Green
        forth_color = "#C2C2C2"  # Silver
        fifth_color = "#212227"  # Black

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.chat_history = QTextEdit(readOnly=True)
        self.layout.addWidget(self.chat_history)

        self.message_input = QLineEdit()
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)

        self.layout.addWidget(self.message_input)
        input_style = f"border: 1px solid {forth_color}; border-radius: 5px; height: 50px;"
        self.message_input.setStyleSheet(input_style)

        style_button = f"background-color: {third_color}; color: #FFF; border-radius: 5px; height: 30px;"
        self.send_button.setStyleSheet(style_button)
        self.layout.addWidget(self.send_button)

    def send_message(self):
        message = self.message_input.text()
        self.chat_history.append(message)
        self.message_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec())
