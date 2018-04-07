import random
 
def checkinformation():
    if random.randint(0,9) > 2:
        global n
        n=n+1
        print(n)
    else:
        if random.randint(0,9) > 5:
            n=n+1
            print(n)
            checkinformation()
        else:
            if random.randint(0,9) > 7:
                n=n+1
                print(n)
                checkinformation()
            else:
                n=n+1
                print(n)
                checkinformation()
global n
n=0
while(1):
    checkinformation()
