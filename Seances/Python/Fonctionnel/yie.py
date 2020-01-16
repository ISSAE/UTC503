def all():
    x=0
    while(True):
        yield x
        x=x+1

def jusqu100():
    x=0
    while(x<100):
        yield x
        x=x+1