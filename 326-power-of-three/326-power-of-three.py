class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        check = 1
        while n >= check:
            if(n==check): return True
            check *= 3
        return False
        