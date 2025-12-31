def reverse_string(s):

    chars = list(s)
    left, right = 0, len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)

if __name__=="__main__":
    s=input("Enter a string: ")
    reversed_s = reverse_string(s)
    print("Reversed string:", reversed_s)

def rev(s):
    char=[]
    
    for i in s:
        char.append(i)
    i=0
    j=len(char)-1
    
    while i<j:
        char[i],char[j]=char[j],char[i]
        i+=1
        j-=1
        
    result=""
    k=0
    while k<len(char):
        result=result+char[k]
        k+=1
    return result
    
print(rev("infosys"))
