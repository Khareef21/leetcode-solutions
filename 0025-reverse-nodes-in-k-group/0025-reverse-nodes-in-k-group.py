# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prevGroup = dummy
        while True:
            kth = prevGroup
            # Find the kth node
            for _ in range(k):
                kth = kth.next
                if kth == None:
                    return dummy.next
            groupNext = kth.next
            # Reverse the current group
            prev = groupNext
            curr = prevGroup.next
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            # Connect the reversed group
            temp = prevGroup.next
            prevGroup.next = kth
            prevGroup = temp
        return dummy.next