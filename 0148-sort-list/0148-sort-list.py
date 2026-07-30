# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        second_head = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(second_head)
        return self.merge(left, right)

    def merge(self, head1, head2):
        dummy = ListNode(0)
        curr = dummy
        while head1 != None and head2 != None:
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
        if head1 != None:
            curr.next = head1
        if head2 != None:
            curr.next = head2
        return dummy.next