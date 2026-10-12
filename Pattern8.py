def pattern8(n):
#n= int(input())
    for i in range(n,0,-1):
        print(' ' *(n-i) + '*' * (2*i -1))
n=int(input("Enter the rows:"))
pattern8(n)