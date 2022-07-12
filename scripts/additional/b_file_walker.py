import os
import subprocess

start_folder = r"D:\DEV\Python\Projects\SA_TEST"

res = []

for root, dirs, files in os.walk(start_folder):
    for file in files:
        file_path: str = os.path.join(root, file)

        if file_path.endswith('.xml'):

            res.append(file_path)
            print(file_path)

pr = subprocess.Popen(["explorer.exe", root], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
stdout, stderr = pr.communicate()
