                                                  #число фибоначи
m = 15
l = [1, 1]
while len(l) <=15:
    l.append((l[-1] + l[-2]))
print(l)

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)
c = fib(10)
print(c)



                                            #колличество элиментов в строке

def str_len(str1):
    c=0
    for i in str1:
        c+=1
    return c

str1="Данил"
print("Ваша строка:", str1)

print("Длинна строки =", str_len(str1))



                                                  # Валидность дата

import time
date = input('Дата (mm/dd/yyyy):')
try:
  valid_date = time.strptime(date, '%m/%d/%Y')
except ValueError:
  print('Не правельтная дата!')