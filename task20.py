'С помощью анонимной функции извлеките из списка числа, делимые на 15.'
spisok = [15,225,300,999,100]
result = list(filter(lambda x: x % 15 == 0, spisok))
print (result)