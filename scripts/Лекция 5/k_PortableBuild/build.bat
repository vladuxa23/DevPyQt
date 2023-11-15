@echo on

chcp 65001

rmdir /S/Q Paint
mkdir Paint

rar.exe x ppython-3.10.11.rar Paint

Paint\python.exe -m pip install -r requirements.txt

xcopy Paint5D.py Paint
xcopy start.bat Paint

pause