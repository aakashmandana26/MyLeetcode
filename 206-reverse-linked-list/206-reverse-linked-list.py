# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        n = head
        arr = []
        while n is not None:
            arr.append(n.val)
            n=n.next
            
        if(len(arr)==0):
            return
        
        newNode = ListNode(None)
        tail = newNode
        i=1
        while(len(arr)-i >=0):
            tail.val=arr[-i]
            i+=1
            if(len(arr)-i < 0):
                break
            tail.next=ListNode()
            tail = tail.next
            
        return newNode
        
        
        
        
        


            
        