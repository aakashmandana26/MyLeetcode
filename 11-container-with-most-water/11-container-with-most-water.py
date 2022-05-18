class Solution:
    def maxArea(self, height: List[int]) -> int:
        
    
        n = len(height)
        s = 0
        e = n-1
        max_area = 0
        while s<e:
            small = height[s] if height[s]<height[e] else height[e]
            area = (e-s)*small
            if area>max_area:
                max_area = area
            if height[s] < height[e]:
                s+=1
            else:
                e-=1
        return max_area
        
            
            
    #     area = 0
    #     for i in range(n-1):
    #         j=i+1
    #         for j in range(n):
    #             small = height[i] if height[i]<height[j] else height[j]
    #             if ((j-i)*small)>area:
    #                 area = (j-i)*small
    #     return area
           
                
        