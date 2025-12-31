def maxsubaarray(arr,k):
    window_sum=0
    i=0
    while i<k:
        window_sum+=arr[i]
        i+=1
    max_sum=window_sum

    i,n=k,len(arr)

    while i<n:
        window_sum=window_sum-arr[i-k]+arr[i]

        if window_sum>max_sum:
            max_sum=window_sum
        i+=1
    return "maxsubarrayk",max_sum

print(maxsubaarray([2, 1, 5, 1, 3, 2],3))