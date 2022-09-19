f = open('1.txt', 'r')
line = f.readlines()
print(type(line))
print(line)
l = f.read()
print(type(l))
print(l)
f = f.close()
print('______________\n_______________')
f = open('1.txt', 'r')
print('f is: ', type(f))
for line in f:
    print(type(line))
    print(line)
f = f.close()

with open('1.txt', 'r') as f:
    line = f.read()
    print(line)

with open('1.txt', 'r') as f:
    line = f.readline()
    print(line)
