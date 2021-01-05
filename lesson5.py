import json
import os

file = input('введите имя создаваемой папки папки в которую будете сохранять файлы ')
try:
    os.mkdir(file)
except FileExistsError:
    iff=input("Такой файл уже существует хотите в нем сохранять свои файлы ?")
    if iff=='да' or iff=='Да':
        file=file
    elif iff=='Нет' or iff=='нет':
        file = input('введите имя создаваемой папки папки в которую будете сохранять файлы ')
        os.mkdir(file)
        
def create():
    name = input('введите имя ')
    surename = input('введите фамилию ')
    age = input('введите год рождения ')
    filename = file + '/' + name + '.txt'

    slovar = {
        'name': name,
        'surname': surename,
        'age': age
    }

    with open(filename, 'w') as f:
        spisok = json.dumps(slovar)
        f.write(spisok)
    print("Файл с данными создан\n")
create()


def vyvod(file=file):

    directory = os.listdir(file)
    for file in directory:
        print('файл с данными пользователя ', file,'\n')


def vybor():

    seach_file = input('введите имя файла которое хотите открыть ')
    seach_file2 = file + '/' + seach_file + '.txt'
    try:
        with open(seach_file2, 'r') as f:
            file_content = f.read()
            saved_dict = json.loads(file_content)
            print('Данные файла', saved_dict)
    except IOError:
        print("Такого файла не существует\n")
        povtor()


def add_main():
    add_data = input('введите имя файла который в который хотите добавить данные ')
    add_data2 = file + '/' + add_data + '.txt'
    with open(add_data2, 'a') as f:
        add = input('введите информацию которую хотите добавить ')
        f.write(add)
        print('Информация добавлена')


def povtor():
    print('если хотите вывод всех файлов с пользователями введите цифру 1')
    print('если хотите выбор файла и вывод данных 2')
    print('если хотите создание новой записи, путем введения новых данных 3')
    print('если хотите создать новый файл 4')
    print('если хотите выйти из программы введите 5')


    comand = int(input())
    if comand == 1:
        vyvod()
    if comand == 2:
        vybor()
    if comand == 3:
        add_main()
    if comand == 4:
        create()
    if comand == 5:
        return
    povtor()
povtor()
