class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = - sys.maxsize -1
        maxSum = currSum - 1
        for i in nums:
            if currSum < 0:
                currSum = i
            else:
                currSum = currSum + i
            maxSum = max(maxSum, currSum)
        return maxSum
