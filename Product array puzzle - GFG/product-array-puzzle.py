#User function Template for python3
# import functools
class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        product0 = 1
        productWithout_0 = 1
        res = []
        count0 = 0
        
        for nums in arr:
            if nums != 0:
                productWithout_0 *= nums 
            else:
                count0 += 1
            product0 *= nums
        if count0>=2:
            res = [0 for i in range(n)]
            return res
        elif count0 == 1:
            for nums in arr:
                if nums==0:
                    res.append(productWithout_0)
                else:
                    res.append(0)
            return res
        else:
            for nums in arr:
                res.append(int(product0/nums))
            return res
        
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends