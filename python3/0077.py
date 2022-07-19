### WIP!

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1,n))
        res = []
        subset = []
        def dfs(i):
            if i == n:
                if len(subset) == k:
                    res.append(subset.copy())
                return
            
            # Decision to include next nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # Decision to NOT include next nums[i]
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res