class Solution:
    def intToRoman(self, num: int) -> str:
        intToRoman={1:"I",
                    4:"IV",
                    5:"V",
                    9:"IX",
                    10:"X",
                    40:"XL",
                    50:"L",
                    90:"XC",
                    100:"C",
                    400:"CD",
                    500:"D",
                    900:"CM",
                    1000:"M"}
        
        if(num in intToRoman.keys()):
            return intToRoman[num]
        else:
            romanStr=""
            while(num>0):
                for key in list(intToRoman.keys())[::-1]:
                    while(num>=key):
                        num=num-key
                        romanStr+=intToRoman[key]
            return romanStr
                        
                    
            
            
#             romanArr=[]
#             romanString=""
#             i=1
#             while(num>0):
#                 digit=(num%10)*i
                
#                 romanArr.insert(0,digit)
#                 num//=10
#                 i*=10
#             for n in romanArr:
#                 if(n in intToRoman.keys()):
#                     romanString += intToRoman[n]
#                 else:
#                     while(n>0):
#                         n=n-
#             return romanString
            
                
                
                
                
            
        
        
        