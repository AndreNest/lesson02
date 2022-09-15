from turtle import down
import lesson02
from lesson020 import printing as prot

colors = ['red', 'white', 'blue']
data = open('file.txt', 'a') # a - дозаписывает, w - перезаписывает 
data.writelines(colors)
data.write('\nLINE 22 \n')
data.write('LINE 33 \n')
data.close()

path = 'file.txt'
data = open(path, 'r') # r - читает
for line in data:
    print(line)
data.close()
tel = 'TEST'
prot(tel)

dictionary = {}
dictionary = \
    {
        'up' : 'вверх',
        'left' : 'влево',
        'down' : 'вниз',
        'right' : 'вправо' 
    }
print(dictionary)
print(dictionary['up'])

colors = {'red', 'green', 'blue'}
print(colors) # {'green', 'red', 'blue'}
colors.add('red')
print(colors) # {'green', 'red', 'blue'}
colors.add('grey')
print(colors) # {'green', 'grey', 'red', 'blue'}
colors.remove('red')
print(colors) # {'green', 'grey', 'blue'}
# colors.remove('red') #KeyError: 'red'
colors.discard('red') #OK
print(colors)
colors.clear() # пустое множество
print(colors)

a = {0, 2, 4, 6, 8, 10, 12, 14}
print(a)
b = {1, 3, 5, 7, 9, 10, 12, 13, 15}
print(b)
c = a.copy()
print(c)
u = a.union(b)
print(u)
i = a.intersection(b)
print(i)
dl = a.difference(b)
print(dl)
dr = b.difference(a)
print(dr)
q = a\
    .union(b) \
        .difference(a.difference(b))
print(q)

s = frozenset(a) # заморозка множества



list1 = [1,2,3,4,5]
list2 = list1
list1[0] = 23
for i in list1:
    print(i)
print()
for i in list2:
    print(i)
print()
print(list1)
list1.append(11)
print(list1)
#print(list1.insert(3, 33))
