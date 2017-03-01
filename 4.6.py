#coding=utf-8
def fib(n):
    a,b=0,1
    result=[]
    while a<n:
        result.append(a)
        a,b=b,a+b
    return result

fib(100)
f=fib
print f(100)