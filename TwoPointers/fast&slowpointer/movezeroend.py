def move_zeroes(arr):
    i = 0
    
    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return arr
    
    
if __name__=="__main__":
    arr = list(map(int,input("enter the input:").split()))
    print(move_zeroes(arr))