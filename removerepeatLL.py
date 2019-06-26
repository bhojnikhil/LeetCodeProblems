# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        c=head
        while c is not None and c.next is not None:
            if(c.val==c.next.val):
                c.next=c.next.next
            else:
                c=c.next
        return head