def pattern18(n):
    for i in range(n):
        for j in range(65+n-1-i,65+n):
            print(chr(j),end=" ")
        print()
n=int(input("Enter the row: "))
pattern18(n)