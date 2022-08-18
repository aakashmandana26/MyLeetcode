class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if(digits[-1]<9):
            digits[-1] += 1
            
        else:
            i=1
            n = len(digits)
            
            while(digits[n-i]==9):
                digits[n-i]=0
                i+=1
                
            if((n-i)>=0):
                digits[n-i] += 1
            else:
                digits.insert(0,1)
            
        return digits
                
                
            
            
            
        
    

        
        
        