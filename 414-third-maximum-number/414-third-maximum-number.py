class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = len(nums)
        firstMax = float('-inf')
        secondMax = float('-inf')
        thirdMax = float('-inf')
        
        for i in range(len(nums)):
            if(nums[i]>firstMax):
                firstMax, secondMax, thirdMax = nums[i], firstMax, secondMax
            elif(nums[i]>secondMax and nums[i]<firstMax):
                secondMax, thirdMax = nums[i], secondMax
            elif(nums[i]>thirdMax and nums[i]<secondMax):
                thirdMax = nums[i]
        
        if(thirdMax==float('-inf')):
            return firstMax
        else:
            return thirdMax
            
        