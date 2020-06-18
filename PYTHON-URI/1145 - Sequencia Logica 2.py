import math

entradas = input().split()
x = int(entradas[0])
y = int(entradas[1])

lin = math.ceil(y/x)

n = 1

for i in range(0,lin,1):
        for j in range(0,x,1):
                if j == x-1:
                        if n <= y:
                                print("%d" %n)
                                n+=1
                        else:
                                break  
                else:
                        
                        if n <= y:
                                print("%d" %n, end=" ")
                                n+=1
                        else:
                                break



