import json

field=[[], [],[]]
i=0;
while i<9:
    stroka = int(input('введите индекс строки'))
    stolb = int(input('введите индекс столбца'))
    if i % 2 == 0:
        if len(field[stroka]) < 3:
            field[stroka].insert(stolb, 'X')
        else:
            print('эта поле уже заполнено')
            i=i-1

    else:
        if len(field[stroka])<3:
            field[stroka].insert(stolb, 'O')
        else:
            print('эта поле уже заполнено')
            i = i - 1
    i+=1
    print(field[0])
    print(field[1])
    print(field[2])

filename='result.json'
with open(filename, 'w') as f:
    json.dump(field,f)
print("Файл с данными создан\n")