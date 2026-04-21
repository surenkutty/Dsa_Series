def twosum(arr,target):
    l,r=0,len(arr)-1
    while l<r:
        s=arr[l]+arr[r]
        if s==target:
            return [l,r]
        elif s<target:
            l+=1
        else:
            r-=1
    return -1


arr=[1,2,3,4,5]
target=5
print(twosum(arr,target))