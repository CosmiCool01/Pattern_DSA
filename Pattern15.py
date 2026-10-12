def pattern15(n):
    for i in range(n):
        for j in range(n-i+1):
            print(chr(65+j),end='')
        print()
n=int(input("Enter the row: "))
pattern15(n)