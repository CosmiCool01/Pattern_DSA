def pattern5( n):
    for i in range(n):
        for j in range(n-i+1):
            print("*",end='')
        print()
n=int(input("Enter the row: "))
pattern5(n)