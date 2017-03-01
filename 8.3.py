import sys
try:
    f=open('myfile.txt')
    s=f.readline()
    i=int(s.strip())
except IOError as err:
    print ("OI Error")
except ValueError:
    print ("Value Error")

for args in sys.argv[1:]:
    try:
        f=open(args,'r')
    except IOError:
        print ("can not open",args)
    else:
        print(args,'has',len(f.readlines()))
        f.close()

try:
    raise Exception('spam','error')
except Exception as inst:
    print (type(inst))
    print (inst.args)
    print (inst)




























