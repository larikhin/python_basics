largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print('Invalid input')
        continue
    if smallest == None:
        largest, smallest = num, num
    if largest < num:
        largest = num    
    if smallest > num:
        smallest = num    
   
print("Maximum is ", largest)
print("Minimum is ", smallest)
