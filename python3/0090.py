# Quick Answer
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [] # final result set
        subset = [] # current subset (mutable)
        def dfs(i):
            if i == len(nums): # if not beyond solution space
                if sorted(subset) not in res:
                    res.append(sorted(subset).copy()) # use .copy() because list is mutable
                return

            # Decision to include next nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Decision to NOT include next nums[i]
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res

# Rethinking solution space
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [] # final result set
        subset = [] # current subset (mutable)
        def dfs(i):
            if i == len(nums): # if not beyond solution space
                res.append(subset.copy()) # use .copy() because list is mutable
                return

            # Decision to include next nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # All subsets that don't include nums[i]
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1 
            dfs(i + 1)
        dfs(0)
        return res

# Could also use a hashmap on seen subsets