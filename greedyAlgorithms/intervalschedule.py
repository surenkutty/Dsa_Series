def max_intervals(intervals):
    intervals.sort(key=lambda x: x[1])

    count=0
    last_end=intervals[0][1]

    for i in range(1,len(intervals)):
        if intervals[i][0]>=last_end:
            count+=1
            last_end=intervals[i][1]
    return count+1

intervals=[[1,3],[2,5],[4,6]]
print(max_intervals(intervals))

'''
The function `max_intervals` takes a list of intervals, where each interval is represented as a list of two integers [start, end]. The goal is to find the maximum number of non-overlapping intervals that can be selected from the given list.
'''

def max_intervals(intervals):
    intervals.sort(key=lambda x: x[1])

    count=0
    last_end=int('-inf')

    for start,end in intervals:
        if start>=last_end:
            count+=1
            last_end=end

    return count

'''
start end its only appilicable  tuples 
like [(1,3),(2,5),(4,6)]
so we can use unpacking in for loop
start,end=intervals[i] is same as start,end in intervals
'''

'-----------------------------'


'''
2. Non-overlapping Intervals (Remove minimum)

👉 Remove minimum intervals to avoid overlap
answer = total_intervals - max_non_overlapping
'''


def eraseOverlapIntervals(intervals):
    # Step 1: sort by end time
    intervals.sort(key=lambda x: x[1])

    count = 0
    last_end = float('-inf')

    # Step 2: find max non-overlapping
    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end

    # Step 3: calculate removals
    return len(intervals) - count


# Example
intervals = [(1,3), (2,4), (3,5)]
print(eraseOverlapIntervals(intervals))  # Output: 1