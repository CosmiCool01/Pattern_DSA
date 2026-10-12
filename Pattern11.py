def pattern11( n):
    for i in range(n):
        for j in range(i+1):
            print((i+j+1)%2,end='')
        print()
n=int(input("Enter the row: "))
pattern11(n)