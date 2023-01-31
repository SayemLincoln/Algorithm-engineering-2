# -*- coding: utf-8 -*-
#Name - Sayem Lincoln
#PID - A54207835 
#CSE 431 Homework 2
# Hybrid sorting algorithm, problem 1

import sys

def merge_sort(left,right):
    """Takes two lists and merge them with merge sort. Returns sorted list"""
    sort = [0] * (len(left) + len(right))
    i=0
    j=0
    k=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sort[k]=left[i]
            i=i+1
        else:
            sort[k]=right[j]
            j=j+1
        k=k+1

    while i<len(left):
        sort[k]=left[i]
        i=i+1
        k=k+1

    while j<len(right):
        sort[k]=right[j]
        j=j+1
        k=k+1

    return sort

def quick_sort(alist):
    """Takes list and divide it on three parts using quick sort."""
    n = len(alist)//2
    alist_left = []
    alist_right = []
    for i in range(len(alist)):
        if i == n: continue
            
        if alist[i] < alist[n]:
            alist_left.append(alist[i])
        else:
            alist_right.append(alist[i])
    return [alist_left, [alist[n],], alist_right]

def hybrid_sort(alist, spec, d=0):   
    """Performs hybrid sort of a list. Particular sorting mehod is specified by user.
    
    Input parameters:
        alist - unorted list
        spec - list of method specifications
        d - recursive depth (by default is 0)
    Output parameters:
        alist - sorted list
        
    """
    if len(alist) <= 1:
        print(spec[d%len(spec)], 0, 0)
        return alist 
    
    if spec[d%len(spec)] == 1:
        d = d+1
        
        mid = len(alist)//2
        left = hybrid_sort(alist[:mid], spec, d)
        right = hybrid_sort(alist[mid:], spec, d)
        print(spec[d%len(spec)], len(left), len(right))
        
        return merge_sort(left, right)
        
    elif spec[d%len(spec)] == 2:
        d = d+1
        
        left = quick_sort(alist)[0]
        right = quick_sort(alist)[2]
        pivot = quick_sort(alist)[1]
        print(spec[d%len(spec)], len(left), len(right))
        
        return hybrid_sort(left, spec, d) + pivot + hybrid_sort(right, spec, d)
    
def read_list(filename):
    """Reads file with input data. Returnes list of integers."""
    f = open(filename,'r')
    alist = []
    for line in f.readlines():
        line = line.split()
        for num in line:
            alist.append(int(num))
    f.close()
    return alist

def write_list(alist, filename):
    """Writes list of integers to the text file."""
    f = open(filename,'w')
    for num in alist:
        f.write(str(num) + "\n")
    f.close()
    
def main():
    
    #parse arguments
    file_in = sys.argv[1]
    file_out = sys.argv[2]
    spec = [int(num) for num in sys.argv[3:]]
    
    #read input list from file
    unsorted_list = read_list(file_in)
    
    #sort list
    sorted_list = hybrid_sort(unsorted_list, spec)
    
    #write sorted list to file
    write_list(sorted_list, file_out)
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

