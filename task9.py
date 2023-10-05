'Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.'
x = int(input())
days = x//(24*3600)
hours = x//3600
minutes = x//60
print (days, hours, minutes)