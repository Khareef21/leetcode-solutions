# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                new_node=head
                while slow!=new_node:
                    slow=slow.next
                    new_node=new_node.next
                return new_node
        return None
            
        