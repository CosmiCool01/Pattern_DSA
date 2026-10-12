def pattern12( n):
    for i in range(1,n+1):        #Numbers
        for j in range(1,i+1):
            print(j,end='')
            #Space
        for s in range(2*(n-i),0,-1):
            print(' ',end='')
            #Numbers2
        for j in range(i,0,-1):
            print(j,end='')
        print()
n=int(input("Enter the row: "))
pattern12(n)