import random as rd
import sys

##This is a simple implementation of quicksort using python##

def quicksort(arrayname):
    middle = int(len(arrayname)/2)
    if middle==0:
        return arrayname
    middleElement = arrayname[middle]
    less = [a for a in arrayname if a<middleElement]
    equals = [a for a in arrayname if a==middleElement]
    more = [a for a in arrayname if a>middleElement]
    less=quicksort(less)
    more=quicksort(more)
    arrayname=less+equals+more
    return arrayname 


if __name__=='__main__':
    x = [rd.randrange(1000) for values in range(100)]
    x=quicksort(x)
    print(x)
