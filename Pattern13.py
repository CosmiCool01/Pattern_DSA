n=int(input("Enter the row: "))
s=0
for i in range(1,n+1):
    for j in range(1,i+1):
        s+=1
        print(s,end=' ')
    print()