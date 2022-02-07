
#Кортеж
'''
vlad = ("vlad", 24, "koval")
name = vlad[1]
print(type(name))

for i in vlad:
    print(i)
'''

#Списки
'''
from copy import copy
i = [1, 2, "vald"]
i1 = copy(i)
i1[2] = 'Hmama'
print(i1)
print(i)
i[0] = "49"
print(i[0])
'''

'''
from copy import deepcopy
i = [[0, "danil"], 1, 2, "vald"]
i1 = deepcopy(i)
i1[2] = 'Hmama'
print(i1)
print(i)
i[0] = "49"
print(i[0])
'''

'''
l = [1, 2, 3, "danil", "dyuzhov"]

l2 = []
for i in l:
    l2.append(i)
print(l2)
'''

'''
l = [1, 2, 3, "danil", "dyuzhov"]
l2 = [item for item in l if item]
print(l2)
'''

'''
l = []
l2 = [i for i in range(0, 100, 3) if i%5 !=0]
print(l2)
'''

l1 = ['papa', 'papas']

# def cmp_list (l1, l2):
#     l3 = [item for item in l1 if item l2]
#     return l3
#
# l = [1, 2, 3, 4, 'sdsds']
# def del_dupl(l):
#     rest_list = []
#     for item in l:
#         if item not in rest_list:
#             rest_list.append(item)
#     return rest_list

# def remove_duplicates():
#     t = ['a', 'b', 'c', 'd']
#     t2 = ['a', 'c', 'd']
#     for t in t2:
#         t.append(t.remove())
#     return t
#     print(t)
#
#
# def nuber(char, string):
#     count = 0
#     for letter in string:
#         if letter == char:
#             count +=1
#     print(string)
#     print('Колличество символа', char, 'состовляет', count)
#
# phrase = 'TeachMeskillse'
# nuber('e', phrase)



# l1 = ["hello", "world", "!"]
# l4 = "".join(l1)
# print(l4)



# def format_date(date):
#     date_list = date.split('/')
#     res_date = '-'.join([date_list[2], date_list[1], date_list[0]])
#     return res_date
# x = format_date("01/02/2022")


# def rever_list(l):
#     return [l[i] for i in range(len(l) -1, -1, -1)]
# x = rever_list("hello")
# print(x)

lis1= [1, 2, 3, 4, 5, 6]
l2 = lis1[::2]
print(l2)
