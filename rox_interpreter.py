import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget
from PyQt6.QtCore import QTimer

class RoxInterpreter:
    def __init__(self):
        self.window = None
        self.widgets = {}

    def run(self, code):
        try:
            exec(self.translate_code(code))
        except Exception as e:
            print(f"Error: {e}")

    def translate_code(self, code):
        translated_code = ""
        lines = code.splitlines()

        for line in lines:
            if "createwindow" in line:
                translated_code += "self.window = QMainWindow()\n"
                translated_code += "self.window.setGeometry(200, 200, 800, 600)\n"
                translated_code += "self.window.show()\n"

            elif "window.screen" in line:
                size = line.split("(")[1].split(")")[0]
                width, height = size.split(",")
                translated_code += f"self.window.setGeometry(200, 200, {width.strip()}, {height.strip()})\n"

            elif "window.background" in line:
                color = line.split("(")[1].split(")")[0].strip("'")
                translated_code += f"self.window.setStyleSheet('background-color: {color};')\n"

            elif "window.createButton" in line:
                args = line.split("(")[1].split(")")[0].split(", ")
                label, x, y = args
                translated_code += f"button = QPushButton('{label.strip()}', self.window)\n"
                translated_code += f"button.move({x.strip()}, {y.strip()})\n"
                translated_code += f"button.show()\n"
                translated_code += f"self.widgets['button'] = button\n"

            elif "window.createLabel" in line:
                args = line.split("(")[1].split(")")[0].split(", ")
                text, x, y = args
                translated_code += f"label = QLabel('{text.strip()}', self.window)\n"
                translated_code += f"label.move({x.strip()}, {y.strip()})\n"
                translated_code += f"label.show()\n"
                translated_code += f"self.widgets['label'] = label\n"

            elif "window.loop" in line:
                translated_code += f"timer = QTimer()\n"
                translated_code += f"timer.timeout.connect(self.update)\n"
                translated_code += f"timer.start(16)\n"  # ~60 FPS

            elif "window.update" in line:
                translated_code += "def update():\n"
                translated_code += line.split("update(")[1].strip() + "\n"

        return translated_code

