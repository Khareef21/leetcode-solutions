# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        curr = head
        length = 1
        while curr.next != None:
            length += 1
            curr = curr.next
        k = k % length
        if k == 0:
            return head
        curr.next = head      # Make circular list
        new_curr = head
        steps = length - k
        for i in range(1, steps):
            new_curr = new_curr.next
        new_head = new_curr.next
        new_curr.next = None

        return new_head