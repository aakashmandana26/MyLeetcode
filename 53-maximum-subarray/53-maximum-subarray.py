
class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        final=nums[0]
        for i in range(len(nums)):
            
            if currSum<0:
                currSum = 0
            currSum+=nums[i]
            final = max(final,currSum)
        return final
            
            
#         final=max[nums]
        
#         for i in range(len(nums)-1):
            
#             if(nums[i]<0):
#                 continue
#             currentSum = nums[i]
            
            
#             for j in range(i+1,len(nums)):
                
#                 currentSum += nums[j]
                
#                 if currentSum<0:
#                     break
               
#                 if currentSum>final:
#                     final=currentSum
                       
#         return final
          
        
            
        
                
                
                
                
        
        