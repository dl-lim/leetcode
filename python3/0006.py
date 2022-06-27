class Solution:
    def convert(self, s: str, n: int) -> str:
        rev = False
        li = []
        pos = 0
        for i in range(0,len(s)): # iterate by length of string
            li.append([pos,i,s[i]])
            if pos == n-1 and n != 1: # Only update at n and 0
                rev = True
            elif pos == 0:
                rev = False

            if rev:
                pos -= 1
            else:
                pos += 1

        result = ''.join([a[2] for a in sorted(li, key = lambda x: (x[0],x[1]))])

        return result
