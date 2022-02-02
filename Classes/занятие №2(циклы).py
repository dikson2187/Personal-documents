'''
x = range(0, 100)
for a in x:
    if a % 3 == 0:
        print(a, "Делится на 3")
    elif a %5 !=0:
        print(a, "Не делится на 5")
'''

'''
i = 0
while i <=100:
    i +=1
    print(i)
'''

'''
i = 0
s = 0
while i <= 100:
    if i % 5 !=0:
        if s + i > 100:
            break
        s += i

    i += 3

print(s)
'''
'''
while True:
    i = 0
    s = 0
    a = int(input("Введите число"))

    while i <= a:
        if i % 5 != 0:
            if s + i > 100:
                    break
            s += i
        i += 3
    else:
        if s + i <=100:
            print("Need more")
            continue
        elif a % 3 != 0:
            print("Need less")
            continue
        print("Exactly")
        print("Sum", s)
        break
'''

'''
i = range(0, 101, 3)
for a in i:
    if a % 5 != 0:
        print(a)

'''


'''
a = str(input("Введите строку"))
b = 0
while True:
    for i in a:
        if i in "aeiouy":
            b += 1
    continue
print("Колличество гласных в слове = ", b)
'''

'''
x = int(input())
for i in range(2, int(x)):
    if x % i == 0:

        print(x, "не простое число")
        break
else:
    print(i, "простое число")
    '''
'''
x = None or 3 and "abc"
print(x)
'''


'''
name = str(input("Введите имя"))
if name == str() or "Word":
    print("Привет", name)
else:
    print("Введите имя")
    '''

a = 'fsd'
print(a.isdigit())