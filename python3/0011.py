class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        r = len(height) - 1
        l = 0
        for _ in range(len(height)-1):
            area = (r - l) * min(height[l],height[r])
            maxarea = max(maxarea,area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxareas
