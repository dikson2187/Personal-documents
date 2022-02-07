#колличество элиментов в строке

def str_len(str1):
    c=0
    for i in str1:
        c+=1
    return c

str1="Данил"
print("Ваша строка:", str1)

print("Длинна строки =", str_len(str1))