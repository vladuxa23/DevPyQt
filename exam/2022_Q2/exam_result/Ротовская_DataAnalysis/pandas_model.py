import pandas as pd


# данный класс расчетный, работа с DataFrame, поэтому ни от кого не наследуюсь
class PandasModel():
    """
     Класс, позволяющий считывать данные форматы .csv и использовать построенную модель
     для построения графиков и проведения расчетов
    """

    def __init__(self):
        self._dataframe = None

    def loadData(self, file_path):
        """
        Функция, читающая данные из формата .csv и преобразующая данные в DataFrame Pandas
        :param file_path: путь до файла
        :return: None
        """
        # читаем файл и получаем названия колонок
        self._dataframe = pd.read_csv(file_path, sep='\t')
        # отфильтровываем колонки ТОЛЬКО числового типа
        numerics = ["int16", "int32", "int64", "float16", "float32", "float64"]
        self._dataframe = self._dataframe.select_dtypes(include=numerics)

    def getColumns(self):
        """
        Функця для получения списка столбцов DataFrame
        :return: список столбцов
        """
        columns = self._dataframe.columns

        return columns

    def getDataShape(self):
        """
        Функция, возвращающая размер DataFrame
        :return: кортеж из двух чисел: (количество строк, количество столбцов)
        """
        return self._dataframe.shape

    def isDataValid(self):
        """
        Функция, проверяющая данные на валидность: файл должен быть непустой, должна быть хотя бы 1 строка
        и 1 столбец
        :return: True, если данные валидны, False в противном случае
        """
        if self._dataframe is not None and self._dataframe.shape[0] > 0 and self._dataframe.shape[1] > 0:
            return True

        return False

    def clear(self):
        """
        Функция очистки объекта DataFrame при загрузке нового файла с данными
        :return: None
        """
        self._dataframe = None

    def getColumnData(self, column):
        """
        Функция, позволяющая получить объект Series: объект данных, состоящих из одной колонки с
        данными по названию столбца
        :param column: названия столбца DataFrame
        :return: объект Series
        """
        data_series = pd.Series(self._dataframe[column])

        return data_series
