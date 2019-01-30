from time import time
tics = []

def tic():
    tics.append(time())

def toc():
    if len(tics)==0:
        return None
    else:
        a = time()-tics.pop()
        print('Elapsed time: '+str(a)+'  seconds')

        return a