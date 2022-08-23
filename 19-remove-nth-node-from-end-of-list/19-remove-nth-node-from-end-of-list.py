# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first=head
        firstCounter=0
        second=head
        secondCounter=0
        tail = head
        while(first.next):
            if(firstCounter-secondCounter != n):
                first=first.next
                
                firstCounter+=1
            else:
                first=first.next
                firstCounter+=1
                second=second.next
                secondCounter+=1
      
        
        if(firstCounter - secondCounter == n):
            second.next=second.next.next
  
        else:
            head=head.next
            
        return head
            
        
        
        
        
            
        