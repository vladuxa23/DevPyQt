"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатие на кнопку
"""
import time
import requests
from PySide6 import QtWidgets, QtCore
from form_weather import Ui_FormWeather
from a_threads import WeatherHandler


class WindowWeather(QtWidgets.QWidget):
    lat = 36.826903
    lon = 10.173742
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui_s = Ui_FormWeather()
        self.ui_s.setupUi(self)
        # self.initThreads()
        self.ui_s.radioButton3.setChecked(True)
        self.ui_s.radioButton3.clicked.connect(self.updateDelay)
        self.ui_s.radioButton5.clicked.connect(self.updateDelay)
        self.ui_s.radioButton10.clicked.connect(self.updateDelay)

        self.ui_s.pushButtonGetData.clicked.connect(self.getData)
        self.ui_s.pushButtonStopGetData.clicked.connect(self.stopGetData)

        self.ui_s.lineEditLatitude.setText("36.826903")
        self.ui_s.lineEditLongitude.setText("10.173742")

        self.ui_s.lineEditLatitude.textChanged.connect(self.validateLatitude)
        self.ui_s.lineEditLongitude.textChanged.connect(self.validateLongitude)

        self.ui_s.lineEditLatitude.textChanged.connect(self.stopGetData2)
        self.ui_s.lineEditLongitude.textChanged.connect(self.stopGetData2)


    def updateDelay(self):
        if self.ui_s.radioButton3.isChecked():
            self.WeatherHandler.setDelay(3)
        elif self.ui_s.radioButton5.isChecked():
            self.WeatherHandler.setDelay(5)
        elif self.ui_s.radioButton10.isChecked():
            self.WeatherHandler.setDelay(10)

    def getData(self):
        # if not valLat:
        #     QtWidgets.QMessageBox.warning("")
        #     return

        WindowWeather.lat = float(self.ui_s.lineEditLatitude.text())
        WindowWeather.lon = float(self.ui_s.lineEditLongitude.text())
        self.WeatherHandler = WeatherHandler(WindowWeather.lat, WindowWeather.lon)
        self.WeatherHandler.setStatus(True)
        self.WeatherHandler.weatherInfoReceived.connect(self.upgradeWeatherInfo)
        self.WeatherHandler.started.connect(lambda: print("Старт потока"))
        self.WeatherHandler.finished.connect(lambda: print("Конец потока"))

        self.ui_s.textEditData.clear()
        self.ui_s.pushButtonGetData.setEnabled(False)
        self.ui_s.pushButtonStopGetData.setEnabled(True)
        self.WeatherHandler.start()

    def stopGetData(self):
        self.WeatherHandler.setStatus(None)
        self.ui_s.pushButtonStopGetData.setEnabled(False)
        self.ui_s.pushButtonGetData.setEnabled(True)

    def stopGetData2(self):
        self.ui_s.textEditData.setText('<font color="red">Координаты изменены</font>')
        self.WeatherHandler.setStatus(None)
        self.ui_s.pushButtonStopGetData.setEnabled(False)
        self.ui_s.pushButtonGetData.setEnabled(True)

    def upgradeWeatherInfo(self, weather_data):
        latitude = weather_data['latitude']
        longitude = weather_data['longitude']
        currentTime = weather_data['current_weather']['time']
        temperature = weather_data['current_weather']['temperature']
        winddirection = weather_data['current_weather']['winddirection']
        windspeed = weather_data['current_weather']['windspeed']
        self.ui_s.textEditData.append(f"Широта: {latitude}, Долгота: {longitude}")
        self.ui_s.textEditData.append(f"Время: {currentTime}")
        self.ui_s.textEditData.append(f"Температура: {temperature}°C")
        self.ui_s.textEditData.append(f"Направление ветра: {winddirection}")
        self.ui_s.textEditData.append(f"Скорость ветра: {windspeed} м/c")


    # def initThreads(self):
    #     self.WeatherHandler = WeatherHandler(
    #     , WindowWeather.lon)
    #     self.WeatherHandler.weatherInfoReceived.connect(self.upgradeWeatherInfo)
    #     self.WeatherHandler.start()

    def validateLatitude(self):
        latitude_text = self.ui_s.lineEditLatitude.text()
        try:
            latitude = float(latitude_text)
            if -180 <= latitude <= 180:
                self.ui_s.lineEditLatitude.setStyleSheet("")
            else:
                self.ui_s.lineEditLatitude.setStyleSheet("background-color: red;")
                self.ui_s.textEditData.setText('<font color="red">Введите корректные координаты</font>')
                self.stopGetData()

        except ValueError:
            self.ui_s.lineEditLatitude.setStyleSheet("background-color: red;")
            self.ui_s.textEditData.setText('<font color="red">Введите корректные координаты</font>')
            self.stopGetData()



    def validateLongitude(self):
        longitude_text = self.ui_s.lineEditLongitude.text()
        try:
            longitude = float(longitude_text)
            if -180 <= longitude <= 180:
                self.ui_s.lineEditLongitude.setStyleSheet("")
            else:
                self.ui_s.lineEditLongitude.setStyleSheet("background-color: red;")
                self.ui_s.textEditData.setText('<font color="red">Введите корректные координаты</font>')
        except ValueError:
            self.ui_s.lineEditLongitude.setStyleSheet("background-color: red;")
            self.ui_s.textEditData.setText('<font color="red">Введите корректные координаты</font>')

class WeatherHandler(QtCore.QThread):
    weatherInfoReceived = QtCore.Signal(dict)

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 10
        self.__status = None

    def setDelay(self, delay) -> None:
        self.__delay = delay

    def setStatus(self, val):
        self.__status = val


    def run(self) -> None:
        while self.__status:
            response = requests.get(self.__api_url)
            data = response.json()
            self.weatherInfoReceived.emit(data)
            time.sleep(self.__delay)





if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = WindowWeather()
    window.show()

    app.exec()