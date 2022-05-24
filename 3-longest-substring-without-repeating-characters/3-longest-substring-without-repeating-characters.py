class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # count = 0
        l=0 
        res=0
        sub=set()
        for i in range(len(s)):
            while s[i] in sub:
                
                sub.remove(s[l])
                l+=1
                
            sub.add(s[i])
            
            
            res= max(res, i-l+1)
        return res
            
                

                    
                
                

                    
            
            
        