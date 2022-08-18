class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        Pointer = 0
        count = 0
        Finalcount = 0
        while(Pointer < len(nums)):
            if(nums[Pointer]==1):
                count+=1
                Pointer +=1
            else:
                Finalcount = max(Finalcount, count)
                count = 0
                Pointer+=1
        
                
        return max(Finalcount, count)
                
            
        