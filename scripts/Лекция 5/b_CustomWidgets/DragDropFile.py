from PySide2 import QtCore, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUi()
        self.updateLabels()

    def initUi(self):
        # main window
        self.setWindowTitle('Drag & Drop')
        self.setGeometry(500, 100, 500, 400)
        self.setAcceptDrops(True) # Даем разрешение на Drop

        # создаём Ui
        self.list_files = QtWidgets.QListWidget()
        self.label_total_files = QtWidgets.QLabel()

        self.tree = QtWidgets.QTreeView()
        self.tree.setSelectionMode(QtWidgets.QTreeView.SingleSelection)
        self.tree.setDragDropMode(QtWidgets.QTreeView.InternalMove)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.tree)
        main_layout.addWidget(QtWidgets.QLabel('Перетащите файл:'))
        main_layout.addWidget(self.list_files)
        main_layout.addWidget(self.label_total_files)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)

        # init models
        model = QtWidgets.QFileSystemModel()
        model.setRootPath(QtCore.QDir.currentPath())

        self.tree.setModel(model)
        self.tree.setRootIndex(model.index(QtCore.QDir.currentPath()))

    def updateLabels(self):
        self.label_total_files.setText('Files: {}'.format(self.list_files.count()))

    def dragEnterEvent(self, event):
        # Тут выполняются проверки и дается (или нет) разрешение на Drop
        mime = event.mimeData()

        # Если перемещаются ссылки
        if mime.hasUrls():
            # Разрешаем действие перетаскивания
            event.acceptProposedAction()

    def dropEvent(self, event):
        # Обработка события Drop
        print(event.mimeData().urls())
        for url in event.mimeData().urls():
            file_name = url.toLocalFile()
            self.list_files.addItem(file_name)

        self.updateLabels()

        return super().dropEvent(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    w = MainWindow()
    w.show()

    app.exec_()
