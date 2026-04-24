def min_flips(bulbs):
    flip_count = 0

    for bulb in bulbs:
        # check effective state
        if (bulb + flip_count) % 2 == 0:
            flip_count += 1

    return flip_count



print(min_flips([1,0, 0, 1,0]))  # Output: 3    



'''Explanation:
The function `min_flips` takes a list of bulbs, where each bulb can be either 0 (off) or 1 (on). The goal is to determine the minimum number of flips required to turn all the bulbs on.
The function initializes a variable `flip_count` to keep track of the number of flips made. It iterates through each bulb in the list, checking its effective state by considering the number of flips made so far. If the effective state of the bulb is off (0), it increments the `flip_count` to flip that bulb and all subsequent bulbs. Finally, it returns the total number of flips needed to turn all bulbs on.
In the example provided, the input list is [0, 1, 0, 1]. The function will determine that the first bulb is off, so it will flip it and all subsequent bulbs, resulting in a flip count of 1. The second bulb is now on, so it will not require a flip. The third bulb is off, so it will require another flip, resulting in a total flip count of 2. The fourth bulb is now on, so it will not require a flip. Therefore, the output of the function will be 2, indicating that a minimum of 2 flips are needed to turn all the bulbs on.

Index	Bulb	flip_count	Effective	Action
0	1	0	(1+0)%2 = 1	சரி ✅ → skip
1	0	0	(0+0)%2 = 0	flip ❌ → count=1
2	0	1	(0+1)%2 = 1	சரி ✅ → skip
3	1	1	(1+1)%2 = 0	flip ❌ → count=2
4	0	2	(0+2)%2 = 0	flip ❌ → count=3