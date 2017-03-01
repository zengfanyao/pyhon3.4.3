# try:
#     raise KeyboardInterrupt
# finally:
#     print ("hello world")
try:
    raise KeyboardInterrupt
except KeyboardInterrupt:
    print ("KeyboardInterrupt")
finally:
    print ("hello world")
