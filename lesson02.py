from turtle import down
import lesson02
from lesson020 import printing as prot

colors = ['red', 'white', 'blue']
data = open('file.txt', 'a')
data.writelines(colors)
data.write('\nLINE 22 \n')
data.write('LINE 33 \n')
data.close()

path = 'file.txt'
data = open(path, 'r')
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


exit()