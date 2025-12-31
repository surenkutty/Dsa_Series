def maxpos(arr):
    curr_sum = 0
    max_sum = 0

    start = 0
    end = 0
    temp_start = 0

    for i in range(len(arr)):
        if arr[i] > 0:
            curr_sum += arr[i]
        else:
            curr_sum = 0
            temp_start = i + 1

        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i

    # Print subarray
    i = start
    while i <= end:
        print(arr[i], end=" ")
        i += 1

    print()
    return max_sum
