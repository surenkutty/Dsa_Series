def maxsubarr(arr):
    curr_sum=arr[0]
    max_sum=arr[0]
    
    start=0
    end=0
    temp_start=0
    
    
    for i in range(1,len(arr)):
        if curr_sum+arr[i]>arr[i]:
            curr_sum=curr_sum+arr[i]
        else:
            curr_sum=arr[i]
            temp_start=i
        
        if curr_sum>max_sum:
            max_sum=curr_sum
            start = temp_start
            end = i

    

    i = start
    while i <= end:
        print(arr[i], end=" ")
        i += 1
        
    return "maxsubarr",max_sum
    

print(maxsubarr([1,2,-3,4,5]))

