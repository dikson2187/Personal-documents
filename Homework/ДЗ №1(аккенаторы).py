var1 =  "Колесо"
var2 =  "Крыша"
flag = 0
print("Какой язык мы изучаем = ?")
while (flag != 1 ):
    choose = input("Ответ: ")
    if (answer1 == choose or answer2 == choose ):
        print("Ваш ответ верен!", choose)
        right+=1
        flag = 1
    else:
        print("Ваш ответ Не верен!")
        print("Какой язык мы изучаем = ?")
        wrong+=1
print("Количество Ваших вариантов: ", right+wrong)
print("Из них правильных: ", right)
print("Из них не правильных: ", wrong)
print("Спасибо большое")