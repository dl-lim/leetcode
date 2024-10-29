# Happy Number!
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        c = 1000
        i = n
        while c > 0:
            i = self.iterate(i)
            if i == 1:
                return True
            c -= 1
        return False
        
    def iterate(self, n):
        lst = [int(e) for e in str(n)]
        k = 0
        for e in lst:
            k += e ** 2
        return k