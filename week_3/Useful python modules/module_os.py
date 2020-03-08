import os

#Return directory current
print(os.getcwd())

#Join string
path = '/image/'
file_name = 'img1.png'
print(os.path.join(path, file_name))

#Split path and file name
path_name = 'PythonAI/AssgignMath/Week_3/module_os.py'
(dir_name, file_name) = os.path.split(path_name)
print(dir_name)
print(file_name)