def pali(s):
    i,j=0,len(s)-1
    is_pal=True
    while i<j:
        if s[i]!=s[j]:
            is_pal=False
            break
        i+=1
        j-=1
    return is_pal

