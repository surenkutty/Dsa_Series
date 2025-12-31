def max_subarray_divisible_by_k(arr, k):
    prefix_sum = 0
    max_sum = 0

    rem_map = {0: 0}  # remainder -> minimum prefix sum

    for num in arr:
        prefix_sum += num
        rem = prefix_sum % k

        if rem in rem_map:
            curr = prefix_sum - rem_map[rem]

            if curr > max_sum:   # instead of max()
                max_sum = curr
        else:
            rem_map[rem] = prefix_sum

    return max_sum
