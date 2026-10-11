
'''for i in range(5):
    for j in range(5):
        print("*",end='')
    print()
'''
def pattern1( n):
    for i in range(n):
        for j in range(n):
            print("*",end='')
        print()
n=int(input("Enter the row: "))
pattern1(n)