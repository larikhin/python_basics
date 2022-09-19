fname = input("Enter file name: ")

fh = open(fname)
lst = list()
for line in fh:
    temp_lst = []
    temp_lst = line.split()
    for item in temp_lst:
        if item not in lst:
            lst.append(item)
lst.sort()
print(lst)

