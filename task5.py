'Найдите три ключа с самыми высокими значениями в словаре my_dict = 'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20'
my_dict = {'a':500, 'c': 560, 'b':5874, 'd':400, 'e':5874, 'f': 20}
result = sorted(my_dict,key=my_dict.get, reverse=True)[:3]
print (result)