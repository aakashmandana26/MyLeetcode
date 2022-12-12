#User function Template for python3

class Solution:
    def Maximize(self, a, n): 
        # Complete the function
        a.sort()
        sum=0
        for i in range(n):
            sum += a[i]*i
        return (sum%(10**9+7) )
            
      



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    print(ob.Maximize(arr, n))
    
# } Driver Code Ends