i=int(input("Enter a number: "))
while(True):
    if i+1<0:
        i=i+1
        continue
    print(i+1, end=" ")
    if(i==99):
        break
    i=i+1
