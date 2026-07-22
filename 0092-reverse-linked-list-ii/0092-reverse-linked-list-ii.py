# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        dummy=ListNode(0)
        dummy.next=head
        prev_left=dummy

        for i in range(1,left):
            prev_left=prev_left.next
        
        #reverse operation
        curr=prev_left.next
        prev=None
        nxt=None
        for i in range(right-left+1):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        #update the values
        left_node=prev_left.next
        prev_left.next=prev
        left_node.next=curr
        return dummy.next

        