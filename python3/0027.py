class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        while k < len(nums):
            if nums[k] == val:
                nums.pop(k
                )
            else:
                k += 1
        return k