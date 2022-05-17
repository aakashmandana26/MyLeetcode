class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        n=len(nums)
        # return n
        
        if (n % 2 == 0):
            median = (nums[int(n/2-1)]+nums[int((n/2+1)-1)])/2
            return median
            
            
        else:
            median = int(((n+1)/2)-1)
            return nums[median]
            
            
        
        