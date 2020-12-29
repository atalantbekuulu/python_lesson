def zapros():
    i = 0
    spisok=[]
    while i < 3:
        marka = input("введите марку авто ")
        model = input("введите модель авто ")
        year = input("введите год авто ")
        i+=1
        slovar={
            "marka":marka,
            "model":model,
            "year":year,
        }
        spisok.append(slovar)
    print(spisok)
zapros()