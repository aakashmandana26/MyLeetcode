class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
     
        anagramDict={}
        res=[]
        for s in strs:
            lst1=list(s)
            lst1.sort()
            str1=''.join(lst1)
            if(str1 not in anagramDict):
                anagramDict[str1]=[s]
            else:
                anagramDict[str1].append(s)
        res.extend(anagramDict.values())
        return(res)

                

        