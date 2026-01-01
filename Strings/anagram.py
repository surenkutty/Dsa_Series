def rem(s1, s2):
    if len(s1) != len(s2):
        return False

    ch1 = {}
    ch2 = {}

    for i in s1:
        if i in ch1:
            ch1[i] += 1
        else:
            ch1[i] = 1

    for j in s2:
        if j in ch2:
            ch2[j] += 1
        else:
            ch2[j] = 1

    if ch1 == ch2:
        return True
    else:
        return False


    
print(rem("ssws","sssw"))