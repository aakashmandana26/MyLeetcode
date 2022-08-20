# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        carry = 0
        while (l1 and l2):
            
            tail.next = ListNode()
            tail = tail.next
            if(l1.val + l2.val + carry <= 9):
                tail.val = l1.val + l2.val + carry
                
                carry = 0
                l1=l1.next
                l2=l2.next

            else:
                tail.val = l1.val + l2.val + carry - 10
                carry = 1
                l1 = l1.next
                l2 = l2.next
            print(tail.val)
            
            # tail.next = ListNode()
            # tail = tail.next
                
                
            
        if(l1):
            while(l1):
                tail.next = ListNode()
                tail = tail.next
                
                if(l1.val + carry < 10):
                    tail.val = l1.val + carry
                    carry = 0
                    
                else:
                    tail.val = l1.val + carry - 10
                    carry = 1
                    
                l1 = l1.next
                    

                
                    
            
        if(l2):
            while(l2):
                tail.next = ListNode()
                tail = tail.next
                
                if(l2.val + carry < 10):
                    tail.val = l2.val + carry
                    carry = 0
                    
                else:
                    tail.val = l2.val + carry - 10
                    carry = 1
                    
                l2 = l2.next

                print(tail.val)
                    
        if(carry==1):
            tail.next = ListNode()
            tail = tail.next
            tail.val = 1
        res = ListNode()
        res=dummy.next
        
        return res
            
    

        