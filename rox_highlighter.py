from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PyQt6.QtCore import QRegularExpression

class RoxSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)

        # Define the format for keywords
        self.keywordFormat = QTextCharFormat()
        self.keywordFormat.setForeground(QColor("red"))  # Set the foreground color to red
        self.keywordFormat.setFontWeight(QFont.Weight.Bold)  # Set the font weight to bold

        # Define the format for strings
        self.stringFormat = QTextCharFormat()
        self.stringFormat.setForeground(QColor("green"))  # Set the foreground color to green

        # Define the format for numbers
        self.numberFormat = QTextCharFormat()
        self.numberFormat.setForeground(QColor("gold"))  # Set the foreground color to blue

        # Define the format for comments
        self.commentFormat = QTextCharFormat()
        self.commentFormat.setForeground(QColor("gray"))  # Set the foreground color to gray
        self.commentFormat.setFontItalic(True)  # Set the font to italic

        # Define the format for brackets
        self.bracketFormat = QTextCharFormat()
        self.bracketFormat.setForeground(QColor("white"))  # Set the foreground color to blue
        self.bracketFormat.setFontWeight(QFont.Weight.Bold)  # Set the font weight to bold

        # Define the list of keywords
        self.keywords = [
            "var", "createwindow", "screen", "background", "createButton", "createLabel", "loop", "update", "window", "Label"
        ]

        # Create a regular expression pattern for keywords
        self.keywordPattern = QRegularExpression(r'\b(' + '|'.join(self.keywords) + r')\b')

        # Create a regular expression pattern for strings
        self.stringPattern = QRegularExpression(r'"[^"]*"')

        # Create a regular expression pattern for numbers
        self.numberPattern = QRegularExpression(r'\b[0-9]+\b')

        # Create a regular expression pattern for comments
        self.commentPattern = QRegularExpression(r'#.*')

        # Create a regular expression pattern for brackets
        self.bracketPattern = QRegularExpression(r'[\(\)\[\]\{\}]')

    def highlightBlock(self, text):
        # Use the regular expression to find keywords
        expression = self.keywordPattern.globalMatch(text)
        while expression.hasNext():
            match = expression.next()
            start_idx = match.capturedStart()
            length = match.capturedLength()
            self.setFormat(start_idx, length, self.keywordFormat)

        # Use the regular expression to find strings
        expression = self.stringPattern.globalMatch(text)
        while expression.hasNext():
            match = expression.next()
            start_idx = match.capturedStart()
            length = match.capturedLength()
            self.setFormat(start_idx, length, self.stringFormat)

        # Use the regular expression to find numbers
        expression = self.numberPattern.globalMatch(text)
        while expression.hasNext():
            match = expression.next()
            start_idx = match.capturedStart()
            length = match.capturedLength()
            self.setFormat(start_idx, length, self.numberFormat)

        # Use the regular expression to find comments
        expression = self.commentPattern.globalMatch(text)
        while expression.hasNext():
            match = expression.next()
            start_idx = match.capturedStart()
            length = match.capturedLength()
            self.setFormat(start_idx, length, self.commentFormat)

        # Use the regular expression to find brackets
        expression = self.bracketPattern.globalMatch(text)
        while expression.hasNext():
            match = expression.next()
            start_idx = match.capturedStart()
            length = match.capturedLength()
            self.setFormat(start_idx, length, self.bracketFormat)