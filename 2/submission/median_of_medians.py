# -*- coding: utf-8 -*-
#Name - Sayem Lincoln
#PID - A54207835 
#CSE 431 Homework 2
# Median of medians algorithm, problem 2


import sys

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

def median_by_sort(l):
    """Finds median in a straitforward way: returns middle member of sorted list 'l'"""
    l = sorted(l)
    return l[len(l) // 2]

def chunked(l, chunk_size):
    """Cuts list 'l' into pieces length chunk_size"""
    return [l[i:i + chunk_size] for i in range(0, len(l), chunk_size)]

def pick_pivot(l, k):
    """
    Function returns pivot for quickselect algorithm using median-of-medians approach
    
    Input: 
        l - list to sort
        k - size of blocks
    Output:
        median_of_medians - pivot to use in quick selection algorithm
    """

    # If there is <5 elements just return median found in straiforward way
    if len(l) < 5:
        return median_by_sort(l)
    
    #Divide list in k-size blocks
    blocks = chunked(l, k)

    #Get rid of the last block if it's size is not k
    last_block = blocks[-1]
    full_blocks = blocks
    if len(last_block) < k:
        full_blocks.pop()

    #Sort each block and find it's median
    medians = [median_by_sort(block) for block in full_blocks]

    #Find the median among block's medians using quickselect algorithm
    median_of_medians = quickselect(medians,k,len(medians) // 2)
    return median_of_medians

def quickselect(l, k, i):
    """
    Function returnes i-th smallest item of given list.
    
    Input:
        l - unsorted list
        k - size of blocks
        i - number of the smallest element to return
    Output:
        The i-th smallest element in 'l'
    """
    if len(l) == 1:
        return l[0]

    #define pivot using median of medians
    pivot = pick_pivot(l,k)
    
    #Divide list into three groups: less, greater and equal to pivot
    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    #Recursively apply function to the part in which our i-th element is.
    if i < len(lows):
        return quickselect(lows,k, i)
    elif i < len(lows) + len(pivots):
        #Stop if it is pivot itself
        return pivots[0]
    else:
        return quickselect(highs,k, i - len(lows) - len(pivots))

def main():
    
    #parse arguments
    file_in = sys.argv[1]
    block_size = int(sys.argv[2])
    stat_number = int(sys.argv[3])
        
    unsorted_list = read_list(file_in)
    
    return quickselect(unsorted_list,block_size,stat_number)
    
    
if __name__ == "__main__":
    ith = main()
    print(ith)
