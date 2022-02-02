                                            #функции

'''
def studens (hi_world, name):
    print(f"{hi_world}, {name}")

studens("danil", "hi")
studens("ivan", "hi")
'''



                                             #Возврат значений функции
'''
def studens (hi_world, name):
    return f"{hi_world}, {name}"

gritings = studens("vlad", "Hi")
print(gritings)
'''


'''
def summa (a, b):
    return a + b

c = summa(5, 2)
print(c)
'''

'''
def has_digit(string):
    for i in range(10):
        if str(i) in string:
            return True
    return False

x = has_digit("1,1,2,2,2")
print(x)
y = has_digit("dsdsds")
print(y)
'''


'''
def is_prime (number):
    for i in range(2, int(number ** 0.5) +1):
        if not number % i:
            return False

    return True

'''

                                            # Находим фактариал числа

'''
def faktarial (namber):
    c = 1
    for i in range(1, namber+1):
        c *=i
    return c

x = faktarial(5)
print(x)


def combinations(n, k):
    c = faktarial(n) / (faktarial(n - k) * faktarial(k))
    return c

d = combinations(3, 2)
print(d)
'''


'''
def hell (hi_world = "Hello", name = "world"):
    return f"{hi_world}, {name}"

print(hell("Hi", "vlad"))
'''


from random import randint as ri
def fact (number: int = 5) ->int:
    '''
     Get number factorial
    '''
    mul = 1 #default value
    for i in range(1, number+1):
        mul *=i
    return mul



x = ri(1, 5)
print(x)

