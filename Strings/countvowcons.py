def counts(s):
    vowels = "aeiouAEIOU"
    v=0
    c=0
    for ch in s:
        if ('a'<=ch<='z') or('A'<=ch<='Z'):
            if ch in vowels:
                v+=1
            else:
                c+=1
    return v,c

s="Hello World! Welcome to DSA Series 123"
v,c=counts(s)
print("Vowels:",v)
print("Consonants:",c)