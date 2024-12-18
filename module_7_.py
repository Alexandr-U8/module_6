import os
# импорт модуля (библиотеки) time для работы с данными времени
import time
# присвоение переменной directory путь до текущего каталога
directory = os.getcwd()
# присвоение переменной directory путь до текущего каталога в папке проекта
# directory = '.'
# обзор всего католага directory организован через несколко циклов в цикле# for i in os.walk(testdir)
for root, dirs, files in os.walk(directory):
    # цикл вывода расположения файлов в directory
    for file in files:
        # присвоение переменной filepath полного пути к итерируемому файлу действием функции join
        filepath = os.path.join(root, file)
        # присвоение переменной filetime
        filetime = os.path.getmtime(filepath)
        # форматирование filetime в удобоваримое значение времени
        formatted_time= time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        # присвоение filesize значения размера файла
        filesize = os.path.getsize(filepath)
        # присвоение parent_dir пути родительской директории
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')