# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        # Create a dummy node which will be the start of our result list
        # We return dummy.next at the end (real head of the result)
        dummy = ListNode(0)           # type: ignore # helper node (value doesn't matter)
        
        # 'current' is the pointer we'll use to build the new list
        current = dummy
        
        # Carry from previous digit addition (0 or 1)
        carry = 0
        
        # We continue as long as:
        # - there are still digits in l1, or
        # - there are still digits in l2, or
        # - there is still a carry left (important for final 9+1 cases)
        while l1 or l2 or carry:
            
            # Get current digit from l1 (use 0 if list already ended)
            x = l1.val if l1 else 0
            
            # Get current digit from l2 (use 0 if list already ended)
            y = l2.val if l2 else 0
            
            # Add digits + carry from previous position
            total = x + y + carry
            
            # New carry for next position (0 or 1)
            carry = total // 10           # integer division → 0 or 1
            
            # Digit we actually write in this position (0-9)
            digit = total % 10
            
            # Create new node with the correct digit
            current.next = ListNode(digit) # type: ignore
            
            # Move our building pointer forward
            current = current.next
            
            # Move to next node in l1 if it exists
            if l1: 
                l1 = l1.next
                
            # Move to next node in l2 if it exists
            if l2: 
                l2 = l2.next
        
        # Return the real head of the result list
        # (we skip the dummy node we created at the beginning)
        return dummy.next