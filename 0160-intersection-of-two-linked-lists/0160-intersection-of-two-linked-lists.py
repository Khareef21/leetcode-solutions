# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if headA == None or headB == None:
            return None

        curr1 = headA
        len_1 = 1
        while curr1.next != None:
            len_1 += 1
            curr1 = curr1.next

        curr2 = headB
        len_2 = 1
        while curr2.next != None:
            len_2 += 1
            curr2 = curr2.next

        curr1 = headA
        curr2 = headB

        if len_1 > len_2:
            diff = len_1 - len_2
            for i in range(diff):
                curr1 = curr1.next
        else:
            diff = len_2 - len_1
            for i in range(diff):
                curr2 = curr2.next

        while curr1 != None and curr2 != None:
            if curr1 == curr2:
                return curr1
            curr1 = curr1.next
            curr2 = curr2.next
        return None