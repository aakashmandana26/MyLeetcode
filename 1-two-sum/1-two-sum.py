class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        x = len(nums)
        lst=[]
        for i in range(x):
            for j in range(i+1,x):
                if(nums[i]+nums[j]==target):
                    lst.append(i)
                    lst.append(j)
        return lst 