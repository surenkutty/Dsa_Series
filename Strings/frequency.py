def counts(s):
    vowels = "aeiouAEIOU"
    v=0
    d=0
    sym=0
    space=0
    let=0
    for ch in s:
        if ('a'<=ch<='z') or('A'<=ch<='Z'):
            let+=1
            if ch in vowels:
                v+=1
        elif '0'<=ch<='9':
            d+=1
        elif ch==" ":
            space+=1
        else:
            sym+=1
    return v,d,sym,space,let

s="Hello World! Welcome to DSA Series 113"
# print(counts(s))
v,d,sym,space,let=counts(s)
print("Vowels:",v)
print("Digits:",d)      
print("Symbols:",sym)
print("Spaces:",space)
print("Letters:",let)   
