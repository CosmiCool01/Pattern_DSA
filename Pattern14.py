def pattern14(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+j),end='')
        print()
n=int(input("Enter the row: "))
pattern14(n)