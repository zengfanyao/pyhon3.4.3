for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print (n,'equlas',x,'*',n//x)
            break
    else:
            print (n,"is a primary number")


for num in range(2,10):
    if num % 2 == 0 :
        print ("Found an even number")
    print("Found a number ,",num)

