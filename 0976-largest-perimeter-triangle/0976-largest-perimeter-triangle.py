class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        count = 0
        perimeter = 0
        i=0
        for num in nums:
            perimeter += num
            count += 1
            
            if(count==3):
                if(perimeter-nums[i]>nums[i]):
                    return perimeter
                else:
                    perimeter = perimeter - nums[i]
                    i+=1
                    
                    count -= 1
        return 0
            
            
            
        
        