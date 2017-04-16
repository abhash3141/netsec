import random as rd


## A short Program that solves selection sort with recursion ##

def selection_sort(arrayname):
    def recursive_selection_sort(arrayname,index):
        ##If the current index is the last index array is sorted
        if index==len(arrayname)-1:
            return
        ##Selection sort always picks the smallest element and keeps it in front
        minimum=arrayname[index]
        minimumIndex=index
        for x in range(index,len(arrayname)):
            if arrayname[x]<minimum:
                minimumIndex=x
                minimum=arrayname[x]
        arrayname[index],arrayname[minimumIndex]=arrayname[minimumIndex],arrayname[index]
        recursive_selection_sort(arrayname,index+1)

    recursive_selection_sort(arrayname,0)



if __name__=='__main__':
    
    x= [rd.randrange(1000) for a in range(100)]
    selection_sort(x)
    print(x)



