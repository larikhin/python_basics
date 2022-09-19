#open file
name = input("Enter file:")
#name = 'mbox-short.txt'

# read line from file
rhand = open(name)

# find From:
senders = dict()
lines_mail = list()
splited_line = list()
for line in rhand:
    if line.startswith('From:'):
        splited_line = line.split()
        lines_mail.append(splited_line[1])
# add to dict or create in dict
for key in lines_mail:
    senders[key] = senders.get(key,0)+1 
#print(senders)
# find maximum
mail = None
mail_value = None
for key in senders:
    if mail is None or senders[key] > mail_value:
        mail = key
        mail_value = senders[key]
   
print(mail, mail_value)

