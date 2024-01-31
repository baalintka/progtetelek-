import math


def oszthatok(szam):
    lista=[]
    i=2
    while(i!=math.sqrt(szam)):
        if szam%i==0:
            lista.append(i)
        i+=1
    return lista

print(oszthatok(10003))

def lineariskereses():
    also:int=0
    felso:int=0
    i=also
    van=True
    while (i<felso) and (i%10!=0):
        i+=1

    van = (i<felso);
    if (van):
        print("van: "+i)
    else:
        print("nincs")