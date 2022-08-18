class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counterPointer = 0
        incrementPointer = 1
        k = 1
        while(incrementPointer < len(nums)):
            if(nums[counterPointer] == nums[incrementPointer]):
                incrementPointer += 1
            else:
                counterPointer += 1
                k+=1
                nums[counterPointer], nums[incrementPointer] = nums[incrementPointer], nums[counterPointer]
                # nums.pop(incrementPointer)
                incrementPointer += 1
        while(len(nums)>k):
            nums.pop()
            
        
        
        
        
            
        