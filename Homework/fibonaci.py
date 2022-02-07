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







                                                