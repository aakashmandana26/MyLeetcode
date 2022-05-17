class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find = {}
        
        for i, n in enumerate(nums):
            if((target-n) in find):
                return (find[target-n],i)
            else:
                find[n]=i
                
#         for i in range(len(nums)):
#             if (nums[i] in find):
#                 return (find[nums[i]],i)
                
#             else:
#                 find[target-nums[i]]=i
        
            
        
                
                
                
                
            
            
            
            
        