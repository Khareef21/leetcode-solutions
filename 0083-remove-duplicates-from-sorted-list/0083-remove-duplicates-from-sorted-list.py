# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #edge cases
        if head==None or head.next==None:
            return head
        curr=head
        while curr!=None and curr.next!=None:
            #duplicate found
            if curr.next.val==curr.val:
                curr.next=curr.next.next
            #not duplicate(unique element)
            else:
                curr=curr.next
        return head


        