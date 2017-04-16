## A simple sorting algorithm ##

import random as rd

def merge_sort(arrayname):
    def sort(arrayname):
        if len(arrayname)==1:
            return arrayname
        a = arrayname[:int(len(arrayname)/2)]
        b = arrayname[int(len(arrayname)/2):]
        return merge(sort(a),sort(b))
    def merge(a,b):
        #length = len(a)+len(b)
        finalarray=[]
        b=[1]
        print(b[0:])
        print(type(finalarray))
        i=0
        j=0
        while True:
            if i==len(a):
                finalarray= finalarray+b[j:]
                break
            elif j==len(b):
                finalarray= finalarray+a[i:]
                break
            elif a[i]<b[j]:
                finalarray = finalarray.append(a[i])
                i+=1
            else:
                finalarray.append(b[j])
                j+=1

    return sort(arrayname)


if __name__=='__main__':
    x= [rd.randrange(1000) for a in range(10)]
    x=merge_sort(x)
    print(x)


                

