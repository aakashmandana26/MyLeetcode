#User function Template for python3

def isSubset( a1, a2, n, m):
    dict={}
    dict2={}
    for num in a1:
        if(num in dict.keys()):
            dict[num]+=1
        else:
            dict[num]=1
    for num2 in a2:
        if(num2 in dict2.keys()):
            dict2[num2]+=1
        else:
            dict2[num2]=1
    for nums in dict2:
        if(nums not in dict or dict2[nums]>dict[nums]):
            return "No"
    return "Yes"
        
        
    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends