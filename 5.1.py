a=[66.25,333,333,1,1234.5]
print a.count(333)
print (a.count(66.25))
print (a.count('x'))
a.insert(2,-1)
print a
a.append(3)
print a
print a.index(3)
print a.index(66.25)
print a.index(333)
a.remove(333)
print a
a.reverse()
print a
print a.sort()
print a
b=a.sort()

squares=[]
for x in range(10):
    squares.append((x**2))

print squares

print [(x,y) for x in [1,2,3] for y in (3,1,4) if x!=y]

combs=[]
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            combs.append((x,y))
print combs

vec=[-4,-2,0,2,4]
print [x*2 for x in vec]
print [x for x in vec if x>0]
print [abs(x) for x in vec]

freshfruit = ['banana','lgoanberry','passwion fruit']

print [weapon.strip() for weapon in freshfruit]
print [(x,x**2) for x in range(6)]

vec=[[1,2,3],[4,5,6],[7,8,9]]

print [num for elem in vec for num in elem]

matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
print [row[1] for row in matrix]

print [[row[i] for row in matrix] for i in range(4)]


td=[]
for i in range(x):
    td.append([wo[i] for wo in matrix])
print td

print list(zip(*matrix))

















