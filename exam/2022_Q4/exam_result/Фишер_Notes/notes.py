### Задача
"""
Реализовать приложение для работы с заметками
Обязательные функции в приложении:
* Добавление, изменение, удаление заметок
* Сохранение времени добавления заметки и отслеживание времени до дэдлайна.
* Реализация хранения заметок остаётся на ваш выбор (БД, json и т.д.).
                """

import datetime
import json

from PySide6 import QtWidgets
from PySide6.QtWidgets import QTreeWidgetItemIterator
from notes_design import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()
        self.unsaved = False
        self.notes_dict = {}
        self.last = None
        self.lastIndex = 0
        self.file = {
            "notes_dict": self.notes_dict,
            "last": self.last
        }

        try:  ## открывает существующий файл
            with open("userFiles/data.json", "r", encoding="utf8") as file:
                self.file = json.load(file)
                self.notes_dict = self.file["notes_dict"]
                self.last = self.file["last"]
                self.redraw_list_menu()
                self.selectItem(self.last)

        except:  ## создает json
            with open("userFiles/data.json", "w", encoding="utf8") as file:
                self.file = {
                    "notes_dict": self.notes_dict,
                    "last": self.last
                }
                json.dump(self.file, file, indent=4)
                self.redraw_list_menu()

    def initSignals(self):
        self.ui.noteHead.textChanged.connect(lambda: self.note_changed())
        self.ui.note_Text.textChanged.connect(lambda: self.note_changed())
        self.ui.saveButton.clicked.connect(lambda: self.save_changes())
        self.ui.delete_Button.clicked.connect(lambda: self.delete_note())
        self.ui.newNoteButton.clicked.connect(lambda: self.newNote())
        self.ui.treeWidget.currentItemChanged.connect(self.load_note)

    def newNote(self):
        """
                Слот для создания новой заметки

                :return: None
                """
        self.ui.noteHead.setPlainText("")
        self.ui.note_Text.setPlainText("")
        self.ui.dateTimeEdit.setDateTime(datetime.datetime.now())

    def save_changes(self):
        """
                        Слот для сохранения заметки

                        :return: None
                        """
        if self.get_note_title() not in list(self.notes_dict.keys()):
            time_now = datetime.datetime.now()
            current_date_seconds_from_start = time_now.timestamp()
            current_date = str(time_now.strftime("%H:%M %d.%m.%Y"))

            if self.get_note_title().strip() == "":
                self.notes_dict["untitled"] = {
                    "title": self.get_note_title(),
                    "date": current_date,
                    "text": self.get_note_text(),
                    "date_to_seconds": current_date_seconds_from_start,
                    "due_date": self.get_due_date()
                }
            else:
                self.notes_dict[self.get_note_title()] = {
                    "title": self.get_note_title(),
                    "date": current_date,
                    "text": self.get_note_text(),
                    "date_to_seconds": current_date_seconds_from_start,
                    "due_date": self.get_due_date()
                }
        else:
            time_now = datetime.datetime.now()
            current_date_seconds_from_start = time_now.timestamp()
            current_date = str(time_now.strftime("%H:%M %d.%m.%Y"))
            self.notes_dict[self.get_note_title()] = {
                "title": self.get_note_title(),
                "date": current_date,
                "text": self.get_note_text(),
                "date_to_seconds": current_date_seconds_from_start,
                "due_date": self.get_due_date()
            }

        self.ui.saveButton.setDisabled(True)
        self.ui.delete_Button.setEnabled(True)
        self.redraw_list_menu()

        with open("userFiles/data.json", "w", encoding="utf8") as file:  ## writing to file
            self.file = {
                "notes_dict": self.notes_dict,
                "last": self.last
            }
            json.dump(self.file, file, indent=4)

    def delete_note(self):
        """
                        Слот для удаления заметки

                        :return: None
                        """
        self.last = None
        if len(self.ui.treeWidget.selectedItems()) != 0:
            note_name = self.ui.treeWidget.selectedItems()[0].text(0)
            if note_name.strip() == "":
                note_name = "untitled"
            self.ui.treeWidget.takeTopLevelItem(
                self.ui.treeWidget.indexOfTopLevelItem(
                    self.ui.treeWidget.selectedItems()[0]
                )
            )
            self.notes_dict.pop(note_name)

        self.ui.noteHead.setPlainText("")
        self.ui.note_Text.setPlainText("")
        self.redraw_list_menu()
        self.ui.delete_Button.setDisabled(True)
        self.ui.saveButton.setDisabled(True)
        with open("userFiles/data.json", "w", encoding="utf8") as file:
            self.file = {
                "notes_dict": self.notes_dict,
                "last": self.last
            }
            json.dump(self.file, file, indent=4)

    def note_changed(self):
        """
                Функция для отображения названия заметки

                :return: None
                """
        if self.get_note_title().strip() == "":
            self.ui.saveButton.setDisabled(True)
        else:
            self.ui.saveButton.setEnabled(True)

    def redraw_list_menu(self):  ## redrawing list one by one
        """
                Функция для отображения заметок  таблице treeWidget

                :return: None
                """
        self.ui.treeWidget.clear()
        for element in list(self.notes_dict.keys()):
            self.last = QtWidgets.QTreeWidgetItem(self.ui.treeWidget,
                                                  [self.notes_dict[element]["title"],
                                                   self.notes_dict[element]["date"],
                                                   self.notes_dict[element]["due_date"]]
                                                  ).text(0)


    def selectItem(self, item_name): ## func to get note from list
        """
                Функция для выбора существующей заметки

                :return: None
                """
        if item_name != None:
            iterator = QTreeWidgetItemIterator(self.ui.treeWidget, QTreeWidgetItemIterator.All)
            while iterator.value():
                item = iterator.value()
                if item.text(0) == item_name:
                    self.ui.treeWidget.setCurrentItem(item, 1)
                    self.load_note(item, None)
                iterator += 1


    def load_note(self, item, last_item):
        """
                        Функция для загрузки существующей заметки

                        :return: None
                        """
        if item != last_item and item != None:
            self.last = item.text(0)
            if item != None:
                current_note_name = item.text(0)
                if current_note_name == "":
                    current_note_name = "untitled"
                current_note = self.notes_dict[current_note_name]
                self.ui.noteHead.setPlainText(current_note["title"])
                self.ui.note_Text.setPlainText(current_note["text"])
                self.setWindowTitle("Note - " + current_note_name)
                self.ui.delete_Button.setEnabled(True)
                self.ui.saveButton.setDisabled(True)

    def get_note_title(self):
        return str(self.ui.noteHead.toPlainText())

    def get_note_text(self):
        return self.ui.note_Text.toPlainText()

    def get_due_date(self):
        return self.ui.dateTimeEdit.text()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
