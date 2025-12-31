def func(arr,k):
    left,curr_sum,max_sum=0,0,0

    for right in range(len(arr)):

        curr_sum+=arr[right]
        
        while curr_sum>=k:
            curr_sum-=arr[left]
            left+=1
        if curr_sum>max_sum:
            max_sum=curr_sum

    return "lesskmaxsubarr",max_sum

print(func([2, 1, 5, 1, 3, 2],7))