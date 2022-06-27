class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            sf = [int(a) for a in str(x)]
            sr = [r for r in reversed(sf)]
            return sf == sr 
