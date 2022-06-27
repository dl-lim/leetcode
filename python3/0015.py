class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)-1):
            seen = set()
            for j in range(i+1,len(nums)):
                r = -(nums[i] + nums[j])

                if r in seen:
                    out = sorted([nums[i], nums[j], r])
                    if out not in result:
                        result.append(out)
                seen.add(nums[j])
        return result
