def zapros():
    spisok=[]
    marka = input("введите марку авто ")
    model = input("введите модель авто ")
    year = input("введите год авто ")
    spisok.append('marka')
    spisok.append(marka)
    spisok.append('model')
    spisok.append(model)
    spisok.append('year')
    spisok.append(year)
    print(spisok)
    slovar = {}
    for index, item in enumerate(spisok):
        if index % 2 == 0:
            slovar[item] = spisok[index + 1]
    print(slovar)
zapros()

