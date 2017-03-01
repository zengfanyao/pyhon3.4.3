tel={'jack':4098,'space':4139}
print tel
print type(tel)
print tel['jack']
del tel['jack']
print tel
tel['irv']=4127
print tel
print list(tel.keys())
print list(tel.values())
print sorted(tel.keys())
print '4127' in tel
print 4127 in tel
print dict([('space',4139),('guido',4127),('jack',4098)])
d={x: x ** 2 for x in (1,2,3)}
print d























