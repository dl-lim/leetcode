# Recursion
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(': ')', 
            '{': '}', 
            '[': ']'
        }
        if len(s) == 0:
            return True
        elif len(s) == 1:
            return False
        else:
            for i in range(len(s)):
                if i+1 < len(s) and s[i] in pairs and s[i+1] == pairs[s[i]]:
                    s = s[0:i] + s[i+2:len(s)]
                    return self.isValid(s)
            return False

# Stack data structure LIFO method
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(', 
            '}': '{',
            ']': '[' 
        }
        stack = []
        for c in s:
            if c in pairs.values():
                stack.append(c)
            else:
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
        return stack == []
