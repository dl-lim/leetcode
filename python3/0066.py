class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i, k = 0, 0
        while i < len(digits):
            j = len(digits) - 1 - i
            k += digits[j] * (10 ** i)
            i += 1
        k += 1
        return [int(d) for d in str(k)]
        
