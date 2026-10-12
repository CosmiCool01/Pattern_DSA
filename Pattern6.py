def pattern6(n):
    for i in range(1,n):
        for j in range(1,n-i+2):
            print(j,end='')
        print()
n=int(input("Enter the rows:"))
pattern6(n)