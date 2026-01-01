def two_sum(nums):
    freq = {}  # number → index
    n=len(nums)
    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
        
    for key in freq:
        if freq[key]>n//2:
            return key
            
    return -1
    


print(two_sum([2,2,3,3,3,3,5]))