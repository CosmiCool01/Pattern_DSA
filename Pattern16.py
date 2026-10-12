def pattern16(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+i),end='')
        print()
n=int(input("Enter the row: "))
pattern16(n)