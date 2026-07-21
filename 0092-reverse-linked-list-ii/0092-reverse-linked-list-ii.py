# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr=head
        list=[]
        while curr!=None:
            list.append(curr.val)
            curr=curr.next
        i=left-1
        j=right-1
        while i<j:
            list[i],list[j]=list[j],list[i]
            i+=1
            j-=1
        curr=head
        for i in range(len(list)):
            curr.val=list[i]
            curr=curr.next
        return head

        