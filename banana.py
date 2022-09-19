'''for letter in 'banana' :
    print(letter)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])
'''

text = "X-DSPAM-Confidence:    0.8475"
item_number =  text.find('0')
number = text[item_number:]
print(float(number))

