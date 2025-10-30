class Solution:
    def isValid(self, s: str) -> bool:
        i=0
        lst=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                lst.append(s[i])
            else:
                if not lst:
                    return False
                top=lst.pop()
                if s[i]==')'and top!='(':
                    return False
                if s[i]==']'and top!='[':
                    return False
                if s[i]=='}'and top!='{':
                    return False
        return len(lst)==0
                
                
                

        