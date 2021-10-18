class Solution:
    def isValid(self, s: str) -> bool:
        valid = False
        plist = list(s)
        pstack = []
        if len(plist) == 1:
            return False
        elif plist[0] in (')', ']', '}'):
            return False

        i = 0
        while i >= 0:
            if len(plist) == 0 and len(pstack) != 0:
                valid = False
                break
            elif len(plist) == 0:
                valid = True
                break
            if plist[i] in ('(', '{', '['):
                pstack.append(plist[i])
                plist.pop(i)
            elif plist[i] in (')', '}', ']') and len(pstack) != 0:
                val = pstack.pop()
                if plist[i] == ')' and val == '(' or plist[i] == ']' and val == '[' or plist[i] == '}' and val == '{':
                    valid = True
                    plist.pop(i) 
                else:
                    valid = False
                    break        
            else:
                valid = False
                break

        return valid

s = "(){}}{"

print(Solution().isValid(s))