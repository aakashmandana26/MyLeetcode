class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x = len(strs)
        common=""
        
        
        strs.sort()
        for i in range(min(len(strs[0]),len(strs[x-1]))):
            if (strs[0][i]==strs[x-1][i]):
                common += strs[0][i]
            else:
                break
        return common
                
        
        
                    
         

        
        
        
        
            
        