ways = []
from tictoc import tic,toc
tic()
for a in range(0,201,200):
    for b in range(0,201-a,100): #representa 100
        for c in range(0,201-a-b,50): #representa 50
            for d in range(0,201-a-b-c,20): #representa 20
                for e in range(0,201-a-b-c-d,10): #representa 10
                    for w in range(0,201-a-b-c-d-e,5):  # representa 5
                        for f in range(0,201-a-b-c-d-e-w,2): #representa 2
                            for g in range(0,201): #representa 1
                                if (200 -a-b-c-d-e-w-f-g== 0):
                                    manera = (a,b,c,d,e,f,g)
                                    ways.append(manera)
toc()
print(len(ways))

str(28433×27830457+1)