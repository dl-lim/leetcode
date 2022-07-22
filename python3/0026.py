class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        stack = []
        if len(nums) == 1:
            stack = nums
        else:
            for h in range(len(nums)):   
                if h == 0 or nums[h] != nums[h-1]:                
                    stack.append(nums[h])           
            for i in range(len(stack)):
                nums[i] = stack[i]
        return len(stack)