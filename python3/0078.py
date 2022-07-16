class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] # final result set
        subset = [] # current subset (mutable)
        def dfs(i):
            if i >= len(nums): # if not beyond solution space
                res.append(subset.copy()) # use .copy() because list is mutable
                return

            # Decision to include next nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Decision to NOT include next nums[i]
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res