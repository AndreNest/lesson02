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


exit()