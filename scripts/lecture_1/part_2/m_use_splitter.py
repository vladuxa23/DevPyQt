"""
Пример работы с QSplitter
"""

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        text_edit_1 = QtWidgets.QTextEdit()  # Создание экземпляра QTextEdit
        text_edit_1.append("text_edit_1")  # Добавление текста в QTextEdit

        text_edit_2 = QtWidgets.QTextEdit()  # Создание экземпляра QTextEdit
        text_edit_2.append("text_edit_2")  # Добавление текста в QTextEdit

        text_edit_3 = QtWidgets.QTextEdit()  # Создание экземпляра QTextEdit
        text_edit_3.append("text_edit_3")  # Добавление текста в QTextEdit

        splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)  # Создание экземпляра QSplitter с вертикальной ориентацией
        splitter.addWidget(text_edit_1)  # Добавление QTextEdit в QSplitter
        splitter.addWidget(text_edit_2)  # Добавление QTextEdit в QSplitter
        splitter.addWidget(text_edit_3)  # Добавление QTextEdit в QSplitter

        splitter.setCollapsible(0, False)  # Отключение "схлопывания" элементов

        layout = QtWidgets.QVBoxLayout()  # Создание экземпляра QVBoxLayout
        layout.addWidget(splitter)  # Добавление QSplitter в QVBoxLayout
        self.setLayout(layout)  # Установка QVBoxLayout для окна


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
