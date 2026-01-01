def removduplicate(s):
    seen=""
    for ch in s:
        if ch not in seen:
            seen+=ch
    return seen

s="programming"
print(removduplicate(s))