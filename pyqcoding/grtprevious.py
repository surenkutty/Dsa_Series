'''
Given an integer array of size N, count elements whose value is
greater than ALL prior elements. The rst element is always counted.
Example:
Input:
5
7
4
8
2
9
Output: 3
'''
def count_greater_than_prior(arr):
    count=0
    max_far=arr[0]
    for i in range(len(arr)):
        if arr[i]>max_far:
            count+=1
            max_far=arr[i]
    return count