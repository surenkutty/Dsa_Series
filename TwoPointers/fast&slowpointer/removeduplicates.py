def removeduplicates(nums):
    slow=0

    for fast in range(1,len(nums)):
        if nums[slow]!=nums[fast]:
            slow+=1
            nums[slow]=nums[fast]
    return slow+1

nums=[1,1,2,2,3]
print(removeduplicates(nums))


def removeduplicates(nums):
    s=[]
    for i in range(len(nums)):
        if nums[i] not in s:
            s.append(nums[i])
    return len(s)