class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
    
        stack = []
        dict = {')':'(', ']':'[', '}':'{'}
        if(s[0]==')' or s[0]==']' or s[0]=='}'):
            return False
        elif (n%2!=0):
            return False
        
        for ch in s:
            if (ch=='(' or ch=='[' or ch=='{'):
                stack.append(ch)
            else:
                if(len(stack)==0):
                    return False
                elif(ch==')' and stack[-1]==dict[')'] or ch==']' and stack[-1]==dict[']'] or ch=='}' and stack[-1]==dict['}'] ):
                    
                    stack.pop()
                    
                else:
                    return False
        if(len(stack)==0):
            return True
                    
                    
                
                    
                    
                    
        
        
                    
                
        