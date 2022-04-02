class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if(s[0]=='-'):
            rev=s[:0:-1]
            if(-2**31 <= int(s[0]+rev) <= (2**31) -1):
            
                return int(s[0]+rev)
            else: 
                return 0
        else:
            rev = s[::-1]
            if(-2**31 <= int(rev) <= (2**31) -1):
                return int(rev)
            else: 
                return 0
        
            
        
        