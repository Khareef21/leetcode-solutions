# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1=self.reverse(l1)
        l2=self.reverse(l2)
        dummy=ListNode(0)
        curr=dummy
        carry=0
        while (l1!=None or l2!=None or carry!=0):
            total=carry
            if l1!=None:
                total+=l1.val
                l1=l1.next
            if l2!=None:
                total+=l2.val
                l2=l2.next
            carry=total//10
            curr.next=ListNode(total%10)
            curr=curr.next
        return self.reverse(dummy.next)
    def reverse(self,head):
        curr=head
        prev=None
        nxt=None
        while curr!=None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev


        