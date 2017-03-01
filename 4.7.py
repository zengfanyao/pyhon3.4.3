#def aks_ok(prompt,retires=4,complain="yes or no please"):
    # while True:
    #     ok=input(prompt)
    #     if ok in ('y','ye','yes'):
    #         return  True
    # if on in ('n','no','nop','nope'):
    #     return False
    # retires=retires - 1
    # if retires == 0 :
    #     raise IOError("refused user")
    # print complain

#aks_ok("Do you want to quit")


def f(a,L=[]):
    L.append(a)
    return L
print f(1)
print f(2)
print f(3)

def g(a,L=None):
    if L is None:
        L=[]
    L.append(a)
    return L
print g(1)
print g(2)
print g(3)

def parrot(voltage,state=' as stiff',action='voom',type="Norweight"):
    print ("--This parrot would not ",action)
    print ("if you put,",voltage,'volts throuht it')
    print ("--Lovely plumage,the",type)
    print ("--It is ,",state)
#parrot(1000)
#parrot(voltage=10000)

parrot(action="VOOOOM",voltage=10000)

def cheeseshop(kind,*args,**keywords):
    print ("--Do you have any",kind,"?")
    print ("-- I am sorry,we are all out of",kind)
    for x in args:
        print x
    print ("--" *40)
    keys=sorted(keywords.keys())
    for x in keys:
        print (x,":",keywords[x])

print "----------------------------------------------------"
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           "Test",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
def concat(seq="/",*args):
    return seq.join(args)

print concat("earth","mars","venus")

print  list(range(3,6))

args=[3,6]
print(list(range(*args)))

def make_incrementor(n):
    return lambda x:x +n
f=make_incrementor(42)
print (f(0))




