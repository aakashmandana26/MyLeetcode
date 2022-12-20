#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    
    def maxSubArraySum(self,arr,N):
        sum = 0
        maxSum = float('-inf')
        ##Your code here
        if max(arr) <= 0:
            return max(arr)
        i=0
        while i<N and arr[i]<=0:
            i+=1
        while i<N:
            sum+=arr[i]
            if(sum<0):
                sum=0
            
            maxSum = max(sum,maxSum)
            i+=1
        return maxSum
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends