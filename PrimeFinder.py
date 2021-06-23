a=int (input("Please, Indicate how many should I calculate prime number"))
b=list(range(2,a+1))
for i in range (2,a+1):
    for j in range (2,i):
        if (i%j==0):
            b.remove(i)
            break
print (b)
