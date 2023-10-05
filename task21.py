'Нужно проверить, все ли числа в последовательности уникальны.'
spisok = [1,2,3,4,5,3]
for i in range(0,len(spisok)):
    for j in range(i+1, len(spisok)):
        if spisok[i] == spisok[j]:
            print("Есть одинаковые")
            quit()
print("Все элементы уникальны")