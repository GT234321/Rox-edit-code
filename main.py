import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QVBoxLayout, QWidget, QMenuBar, QFileDialog, QTabWidget
from PyQt6.QtGui import QFont
from rox_highlighter import RoxSyntaxHighlighter
from rox_interpreter import RoxInterpreter

class CodeEditor(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.setFont(QFont("Consolas", 12))
        self.highlighter = RoxSyntaxHighlighter(self.document())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ROX Code Editor")
        self.setGeometry(200, 200, 800, 600)

        self.editor = CodeEditor()
        self.setCentralWidget(self.editor)

        self.menu = self.menuBar()
        file_menu = self.menu.addMenu("File")

        open_action = file_menu.addAction("Open")
        open_action.triggered.connect(self.open_file)

        save_action = file_menu.addAction("Save")
        save_action.triggered.connect(self.save_file)

        run_action = file_menu.addAction("Run")
        run_action.triggered.connect(self.run_code)

        self.interpreter = RoxInterpreter()

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "ROX Files (*.rox);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'r') as file:
                self.editor.setPlainText(file.read())

    def save_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "ROX Files (*.rox);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'w') as file:
                file.write(self.editor.toPlainText())

    def run_code(self):
        code = self.editor.toPlainText()
        self.interpreter.run(code)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
