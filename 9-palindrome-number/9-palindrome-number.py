class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        m=x
        count=0
        rem=0
        if(x<0):
            return False
        else:
            while(n//10 != 0):
                n //= 10
                count += 1
            while(count>=0):
                rem += m%10 * (10**count)
                m //= 10
                count -= 1
            return (rem == x)

            