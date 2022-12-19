#User function Template for python3


class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        num_dict={}
        count = 0
        ratio = int(n/k)
        for num in arr:
            if num in num_dict.keys():
                num_dict[num]+=1
            else:
                num_dict[num]=1
        
        for nums in num_dict:
            if num_dict[nums]>ratio:
                count+=1
        return count
                
            
        #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=list(map(int,input().split()))
            
            K=int(input())
            
            print(Solution().countOccurence(A, N, K))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends