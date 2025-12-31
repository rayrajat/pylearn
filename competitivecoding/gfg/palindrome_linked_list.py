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

    def isPalindrome(self, head):
        # Edge cases
        if head is None or head.next is None:
            return True

        slow = head
        fast = head

        # Find middle
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        second = self.reverse(slow.next)
        slow.next = None   # break list

        # Compare halves
        first = head
        temp = second
        while temp:
            if first.data != temp.data:
                return False
            first = first.next
            temp = temp.next

        return True