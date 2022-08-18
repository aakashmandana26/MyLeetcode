class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # firstPointer = 0
        secondPointer = 0
        count = 0
        countArr = []
        while(secondPointer < len(nums)):
            if(nums[secondPointer]==1):
                count+=1
                # firstPointer = secondPointer
                secondPointer +=1
            else:
                countArr.append(count)
                count = 0
                secondPointer+=1
        countArr.append(count)
                
        return max(countArr)
                
            
        