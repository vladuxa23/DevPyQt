import matplotlib

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PySide2 import QtWidgets

matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):
    """
    Класс, выделяющий место для построения графика
    """

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class WindowPlotModel(QtWidgets.QWidget):
    """
    Класс, который позволяет строить графики разных типов: Hist, Boxplot, Plot
    """

    def __init__(self, parent):
        super(WindowPlotModel, self).__init__(parent)

        # создаем объект maptlotlib FigureCanvas, который опреляет оси, как self.axes.
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.sc)
        self.setLayout(main_layout)
        self.show()

    def buildGraphHist(self, data, column):
        """
        Функция, позволяющая построить гистрограмму Hist
        :param data: объект Series по выбранной пользователем колонке
        :param column: название столбца
        :return:
        """
        # чистка объекта для построения графика от предыдущих данных
        self.sc.axes.cla()
        # построение гистограммы Hist с набором корзин: 100, и значения по оси x до 90% квартиля
        self.sc.axes.hist(data, bins=100, range=(0, data.quantile(0.9)))
        # устанавливаем название графика
        self.sc.axes.set_title(column)
        # перерисовка графика
        self.sc.draw()

    def buildGraphBoxplot(self, data, column):
        """
        Функция, позволяющая строить ящик с усами Boxplot
        :param data: объект Series
        :param column: название столбца
        :return:
        """
        # чистка объекта для построения графика от предыдущих данных
        self.sc.axes.cla()
        # построение графика Boxplot по данным, отличным от nan
        self.sc.axes.boxplot(data[data.isna() == False])  # не по PEP8, сделала стандартную для Pandas фильтровку от nan
        # устанавливаем название графика
        self.sc.axes.set_title(column)
        # перерисовка графика
        self.sc.draw()

    def buildGraphPlot(self, data, column):
        """
        Функция, позволяющая построить график Plot
        :param data: объект Series
        :param column: название столбца
        :return:
        """
        # чистка объекта для построения графика от предыдущих данных
        self.sc.axes.cla()
        # построение графика Plot
        self.sc.axes.plot(data)
        # устанавливаем название графика
        self.sc.axes.set_title(column)
        # перерисовка графика
        self.sc.draw()
