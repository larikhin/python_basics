rhand = open('text.txt')

# finding some line
for line in rhand:
    if line.startswith('скрипта'):
        print(line)

# reading file like line
one_line = rhand.read()
print(one_line)
print(rhand)


