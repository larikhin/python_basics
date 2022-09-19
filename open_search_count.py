# Use the file name mbox-short.txt as the file name

while True:
    fname = input("Enter file name: ")
#    fname = 'mbox-short.txt'
    try:
        fh = open(fname)
        break
    except:
        pritn('wrong file name')

counter = 0
value = None
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    temp_value = float(line[19:])
    if value == None:
        value = temp_value
    else:    
        value = value + temp_value
    counter = counter +1
    mid_value = value / counter
print('Average spam confidence:', mid_value)
