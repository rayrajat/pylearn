class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def addTwoLists(self, head1, head2):
        
        head1 = self.reverse(head1)
        head2 = self.reverse(head2)

        carry = 0
        dummy = Node(0) # type: ignore
        cur = dummy

        while head1 or head2 or carry:
            v1 = head1.data if head1 else 0
            v2 = head2.data if head2 else 0

            total = v1 + v2 + carry
            carry = total // 10

            cur.next = Node(total % 10) # type: ignore
            cur = cur.next

            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next

        res = self.reverse(dummy.next)

    
        while res and res.data == 0:
            res = res.next

        
        return res if res else Node(0) # type: ignore