import random as rd

def insertion_sort(array):
    last_index = len(array)-1
    def recursion_sort(array,last_index):
        if(last_index==0):
            return
        recursion_sort(array,last_index-1)
        value = last_index
        while value>0 and array[value]<array[value-1]:
            array[value],array[value-1]=array[value-1],array[value]
            value-=1
    recursion_sort(array,last_index)


if __name__=='__main__':
    x= [rd.randrange(1000) for y in range(100)]
    insertion_sort(x)
    print(x)
