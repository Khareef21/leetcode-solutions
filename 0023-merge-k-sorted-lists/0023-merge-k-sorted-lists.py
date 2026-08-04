# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        res=lists[0]
        for i in range(1,len(lists)):
            res=self.merge(res,lists[i])
        return res

    def merge(self,list1,list2):
        dummy=ListNode(0)
        curr=dummy
        while list1!=None and list2!=None:
            if list1.val<=list2.val:
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next
        if list1!=None:
            curr.next=list1
        if list2!=None:
            curr.next=list2
        return dummy.next



        