class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        check = 1
        while n >= check:
            if(n==check): return True
            check *= 2
        return False
    
            
        