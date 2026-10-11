def pattern3(n):
    for i in range(1,n+2):
        for j in range(1,i):
            print(j,end='')
        print()
n=int(input("Enter the rows:"))
pattern3(n)