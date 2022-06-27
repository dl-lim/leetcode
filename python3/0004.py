#import statistics
import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        allnum = sorted(nums1 + nums2)
        if len(allnum) % 2 == 1:
            medpt = int(math.ceil(len(allnum)/2)-1)
            print(medpt)
            result = allnum[medpt]
        else:
            medpt = int(len(allnum)/2-1)
            result = (allnum[medpt] + allnum[medpt + 1])/2
        return result

#        allnum = nums1 + nums2
#        result = statistics.median(allnum)
#        return resultss
