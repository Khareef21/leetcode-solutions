class Solution:
    def reverse(self, head):
        curr = head
        prev = None
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        second = self.reverse(slow)
        first = head
        while second != None:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True