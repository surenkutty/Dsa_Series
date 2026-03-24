'''
Problem Statement:
Given a string S consisting of '*' and '#' characters, nd the minimum
number of characters to add to make it balanced (equal number of
both characters).
'''
def min_characters_to_add(S):
    count_star = S.count('*')
    count_hash = S.count('#')
    
    # Calculate the difference between the counts
    difference = abs(count_star - count_hash)
    
    return difference

    # or

def min_characters_to_add(S):
    star=0
    hash=0
    for c in S:
        if c=='*':
            star+=1
        elif c=='#':
            hash+=1
    return abs(star-hash)