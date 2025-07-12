import sys
import asyncio
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import Qt
import sys
import asyncio
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import Qt
import yaml
import os
import importlib.util
import pathlib

# Dynamically import mistral_model.py from ai-model folder
ai_model_path = pathlib.Path(__file__).parent.parent / "ai-model" / "mistral_model.py"
spec = importlib.util.spec_from_file_location("mistral_model", str(ai_model_path))
mistral_model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mistral_model)
Mistral7BLocal = mistral_model.Mistral7BLocal

class MadhavGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Madhav Personal Assistant")
        self.setGeometry(100, 100, 600, 400)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.status_label = QLabel("Status: Ready")
        self.layout.addWidget(self.status_label)

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.layout.addWidget(self.chat_display)

        self.input_line = QLineEdit()
        self.input_line.setPlaceholderText("Type your message here...")
        self.layout.addWidget(self.input_line)

        self.send_button = QPushButton("Send")
        self.layout.addWidget(self.send_button)

        self.send_button.clicked.connect(self.on_send)
        self.input_line.returnPressed.connect(self.on_send)

        self.model = Mistral7BLocal()

    def append_chat(self, role: str, message: str):
        self.chat_display.append(f"<b>{role}:</b> {message}")

    def on_send(self):
        user_text = self.input_line.text().strip()
        if not user_text:
            return
        self.append_chat("User", user_text)
        self.input_line.clear()
        self.status_label.setText("Status: Thinking...")
        asyncio.create_task(self.get_response(user_text))

    async def get_response(self, user_text: str):
        try:
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(None, self.model.generate_response, user_text)
            self.append_chat("Madhav", response)
        except Exception as e:
            self.append_chat("Error", str(e))
        finally:
            self.status_label.setText("Status: Ready")

def main():
    app = QApplication(sys.argv)
    window = MadhavGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
import yaml
import os

class MadhavGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Madhav Personal Assistant")
        self.setGeometry(100, 100, 600, 400)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.status_label = QLabel("Status: Ready")
        self.layout.addWidget(self.status_label)

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.layout.addWidget(self.chat_display)

        self.input_line = QLineEdit()
        self.input_line.setPlaceholderText("Type your message here...")
        self.layout.addWidget(self.input_line)

        self.send_button = QPushButton("Send")
        self.layout.addWidget(self.send_button)

        self.send_button.clicked.connect(self.on_send)
        self.input_line.returnPressed.connect(self.on_send)

        self.model = Mistral7BLocal()

    def append_chat(self, role: str, message: str):
        self.chat_display.append(f"<b>{role}:</b> {message}")

    def on_send(self):
        user_text = self.input_line.text().strip()
        if not user_text:
            return
        self.append_chat("User", user_text)
        self.input_line.clear()
        self.status_label.setText("Status: Thinking...")
        asyncio.create_task(self.get_response(user_text))

    async def get_response(self, user_text: str):
        try:
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(None, self.model.generate_response, user_text)
            self.append_chat("Madhav", response)
        except Exception as e:
            self.append_chat("Error", str(e))
        finally:
            self.status_label.setText("Status: Ready")

def main():
    app = QApplication(sys.argv)
    window = MadhavGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
