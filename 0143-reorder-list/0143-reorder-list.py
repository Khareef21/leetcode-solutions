# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next==None or head.next.next==None:
            return 
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        #reverse
        curr=second
        prev=None
        nxt=None
        while curr!=None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        
        head1=head
        head2=prev
        while head2!=None:
            next1=head1.next
            head1.next=head2

            next2=head2.next
            head2.next=next1

            head1=next1
            head2=next2

        