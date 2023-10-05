'Вы принимаете от пользователя последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами.'
values = input()
zapit = values.split(',')
num = map(int, zapit)
lst = list(num)
tup = tuple(lst)
print (lst)
print (tup)