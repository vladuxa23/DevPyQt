from PySide2 import QtWidgets, QtGui, QtCore

from ui.data_analysis import Ui_Form
from ui import my_res
from graph_building_model import WindowPlotModel

from pandas_model import PandasModel


class MyAppDataAnalysis(QtWidgets.QWidget):
    """
    Класс, позволяющий пользователю по выбранным данным строить графики и получать расчетную информацию
    для для дальнейшего ее использования в анализе данных и data science
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # зарегистрировали форму
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # арегистрировали модель для построения графика и разместили на форме
        self.graph = WindowPlotModel(self)
        self.ui.verticalLayout_5.insertWidget(0, self.graph)
        # зарегистрировали модель Pandas для получения данных
        self.model = PandasModel()
        # до выбора данных сделали невидимыми другие страницы формы ToolBox
        self.ui.toolBox.setItemEnabled(1, False)

        self.unitUi()

    def unitUi(self):
        # установили заголовок окна программы
        self.setWindowTitle("Программа для первичного анализа данных")
        # установили сигнал для кнопки Звгрузить файл
        pb_choose_get_data = self.ui.pushButtonChooseFile
        pb_choose_get_data.clicked.connect(self.onPushButtonChooseFileGetDataClicked)
        # установили сигнал для кнопки Построить график
        pb_build_graph = self.ui.pushButtonBuildGraph
        pb_build_graph.clicked.connect(self.onPushButtonBuildGraphClicked)
        # устанавливаем иконку на окошко приложения
        my_res.qInitResources()
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/img/my_res/icon.png")))
        # делаем недоступной кнопку Построения графика в момент загрузки приложения
        self.ui.pushButtonBuildGraph.setEnabled(False)

    def onPushButtonChooseFileGetDataClicked(self):
        """
        Функция сигнала при нажатии на кнопку Загрузить файл
        :return:
        """
        # очищаем предыдущие данные
        self.clearAll()
        # делаем недоступной вторую страницу с расчетами
        self.ui.toolBox.setItemEnabled(1, False)
        # делаем недоступной кнопку Построить график, пока пользователь не выбрал файл
        self.ui.pushButtonBuildGraph.setEnabled(False)
        # получаем путь к файлу с данными, выбрать можем только файлы формата .csv
        [file_path, _] = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть файл", "ui", "Данные(*.csv)")
        # делаем проверку, выбрал пользователь файл или нет
        if len(file_path) == 0:
            return
        # передаем данные в pandasModel
        self.model.loadData(file_path)
        # проверям данные на валидность
        is_input_data_valid = self.model.isDataValid()

        if not is_input_data_valid:
            return
        # делаем кнопку построения графика видимой, когда пользователь выбрал валтдный файл
        self.ui.pushButtonBuildGraph.setEnabled(True)
        # прописываем в строке выбора файла его директорию
        self.ui.lineEditChooseFile.setText(file_path)
        # загружаем название столбцов DataFrame
        loaded_columns = self.model.getColumns()
        # передаем название столбцов в checkbox для возможности выбора пользователем столбцов
        self.ui.comboBoxChooseColumn.addItems(loaded_columns)

    def onPushButtonBuildGraphClicked(self):
        """
        Функция сигнала при нажатии на кнопку Построить график
        :return:
        """
        # получаем название столбца, выбранного пользователем
        column = self.ui.comboBoxChooseColumn.currentText()
        # передаем название выбранного столбца в pandasModel для построения объекта Series
        column_data = self.model.getColumnData(column)
        # строим необходимый график по выбранному столбцу и заполняем статистическую информацию
        self.updateGraph(column_data, column)
        self.updateStatistics(column_data)
        # переключаем на вторую страницу ToolBox
        self.ui.toolBox.setCurrentIndex(1)
        self.ui.toolBox.setItemEnabled(1, True)

    def updateGraph(self, column_data, column):
        """
        Функция, позволяющая строить графики при его выборе
        :param column_data: объект Series, на основании которого строится график
        :param column: название столбца, по которому необходимо посторить график
        :return:
        """

        if self.ui.radioButtonHist.isChecked():
            self.graph.buildGraphHist(column_data, column)
        elif self.ui.radioButtonBoxplot.isChecked():
            self.graph.buildGraphBoxplot(column_data, column)
        elif self.ui.radioButtonPlot.isChecked():
            self.graph.buildGraphPlot(column_data, column)

    def updateStatistics(self, column_data):
        """
        Функция, заполняющая статистические данные на итоговой странице формы
        :param column_data: объект Series, на основании которого заполняются данные
        :return:
        """
        self.ui.lineEditCountIsna.setText(str(column_data.isna().sum()))
        self.ui.lineEditPercentIsna.setText(str(f"{round((column_data.isna().sum() / self.model.getDataShape()[0] * 100), 2)}"))
        self.ui.lineEditMin.setText(str(round(column_data[column_data.isna() == False].values.min())))
        self.ui.lineEditMax.setText(str(round(column_data[column_data.isna() == False].values.max())))
        self.ui.lineEditAvg.setText(str(round(column_data[column_data.isna() == False].mean(), 2)))
        self.ui.lineEditMedian.setText(str(round(column_data[column_data.isna() == False].median(), 2)))
        self.ui.lineEditInterquanlileRange.setText(str(round((column_data.quantile(0.75) - column_data.quantile(0.25)), 2)))
        self.ui.lineEditQuantile.setText(str(round(column_data.quantile(0.95), 2)))
        # применяем метод для замены цвета текста в определенной ячейке
        self.updateColorPercentIsna()

    def updateColorPercentIsna(self):
        """
        Функция, позволяющая менять цыет значений в расчетной ячейке: на красный или
        зеленый в зависимости от условия
        :return:
        """
        # устанавливаем палетту
        palette = QtGui.QPalette()
        # задаем условия
        if float(self.ui.lineEditPercentIsna.text()) < 10.0:
            # устанавливаем нужный цвет
            palette.setColor(QtGui.QPalette.Text, QtGui.QColor("green"))
        elif float(self.ui.lineEditPercentIsna.text()) >= 10.0:
            palette.setColor(QtGui.QPalette.Text, QtGui.QColor("red"))
        # применяем палетту к нужной ячейке
        self.ui.lineEditPercentIsna.setPalette(palette)

    def clearAll(self):
        """
        Функция, которая очищает модели от старых значений, при выборе пользователем новых данных
        :return:
        """
        self.model.clear()
        self.ui.comboBoxChooseColumn.clear()
        self.ui.lineEditChooseFile.clear()


class MovieSplashScreen(QtWidgets.QSplashScreen):
    """
    Класс для запуска анимированной заставки до загрузки приложения
    """
    def __init__(self, path_to_gif):
        # задаем объект для работы с gif и передаем ему файл gif
        self.movie = QtGui.QMovie(path_to_gif)
        # переход к следующему номеру кадра, начинаем с 0
        self.movie.jumpToFrame(0)
        # возвращает размер кадра
        pixmap = QtGui.QPixmap(self.movie.frameRect().size())
        # передаем текущий кадр
        QtWidgets.QSplashScreen.__init__(self, pixmap)
        # переход к следующему кадру
        self.movie.frameChanged.connect(self.repaint)

    def showEvent(self, event):
        """
        Функция, которая отвечает за начала показа заставки
        :param event: запуск приложения
        :return:
        """
        self.movie.start()

    def hideEvent(self, event):
        """
        Функция, которая отвечает за выключение загрузки
        :param event: загрузка основного окна
        :return:
        """
        self.movie.stop()

    def paintEvent(self, event):
        """
        Функция, отвечающая за прорисовку заставки
        :param event:
        :return:
        """
        painter = QtGui.QPainter(self)
        pixmap = self.movie.currentPixmap()
        self.setMask(pixmap.mask())
        painter.drawPixmap(0, 0, pixmap)
        # указываем цвет текста надписи
        color = QtCore.Qt.white
        # передаем цвет для прорисовки
        painter.setPen(QtGui.QPen(color))
        painter.setBrush(QtGui.QBrush(color))
        painter.drawText(QtCore.QPoint(20, 20), "Ротовская Евгения")


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    splash = MovieSplashScreen(':/img/my_res/appscreen.gif')
    splash.show()
    win = MyAppDataAnalysis()

    # эмулируем загрузку приложения с ожиданием
    def showWindow():
        splash.hide()
        win.show()

    QtCore.QTimer.singleShot(3000, showWindow)
    app.exec_()
