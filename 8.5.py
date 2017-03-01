
class MyError(Exception):
    def __init__(self,value):
        self.value=value

    def __str__(self):
        return repr(self.value)
try:
    raise MyError(2*2)
except MyError as e:
    print ("My exception occured ,vakue",e.value)

class Error(Exception):
    pass

class InputError(Exception):

    def __init__(self,expression,message):
        self.expression=expression
        self.message=message


class TranslationError(Exception):
    def __init__(self,previous,next,message):
        self.previous=previous
        self.next=next
        self.message=message



























