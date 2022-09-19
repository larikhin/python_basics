name = input("Enter file:")
#name = 'mbox-short.txt'

rhand = open(name)
dict_t = {}
for line in rhand:
    if line.startswith('From '):
        line_sorted = line.split()
        time = line_sorted[5]
        time = time.split(':')
        hour = time[0]
        dict_t[hour] = dict_t.get(hour, 0) + 1

dict_t = [[k, v] for k, v in sorted(dict_t.items())]
for k,v in dict_t:
    print(k,v)
        

