'''
famili = input("Введите свою Фамилию:")

name = input("Введите свое Имя:")

yar = int(input("Введите свой год:"))

vozrs = 2022 - yar

print(vozrs)
status = input("Вы женаты:")
info = f"{famili} {name} {vozrs} {status}"
print(info)
'''


'''
x = int(input())
if x == 10:
    print("yes")
elif x == 6:
    print("yesssss")
else:
    print('no')
'''

'''
yer = int(input("введите год олимпиады"))

if yer % 4 == 0:
    print("Летняя олимпиада")
elif yer % 2 == 0:
    print("Зимняя олимпиада")
else:
    print("небыло ничего")
'''
'''
yer = int(input("введите год"))

if yer % 4 == 0:
    print("высокосный")
elif yer % 100 != 0:
    print("обычный")
'''

yer = int(input('введите возрос'))

if yer == 18:
    print('Вам я продам пиво')
elif  yer <18:
    print("Я не продам вам пиво")