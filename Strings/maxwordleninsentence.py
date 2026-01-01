def func(s):
    max_len=0
    word=""
    curr=""
    
    for ch in s:
        if ch!=' ':
            curr+=ch
        else:
            if len(curr)>max_len:
                max_len=len(curr)
                word=curr
            curr=""
            
    if len(curr)>max_len:
            max_len=curr
    return word
    
print(func("hello i hii"))