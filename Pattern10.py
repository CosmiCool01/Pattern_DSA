def pattern10(n):
#n= int(input())
    for i in range(n):
        for j in range(i+1):
            print('*',end='')
        print()
    for i in range(n):
        for j in range(n-i+1):
            print('*' ,end='')
        print()
n=int(input("Enter the rows:"))
pattern10(n)