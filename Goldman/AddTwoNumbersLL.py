class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        dummy=l1
        while(l1):
            if (l1.val if l1 else 0) +(l2.val if l2 else 0) > 9:
                carry=(l1.val+l2.val)/10
                l1.val= (l1.val+l2.val)%10
            else:
                l1.val= carry+(l1.val if l1 else 0)+(l2.val if l2 else 0)
                carry=0
            l1=l1.next
            l2=l2.next
        return dummy

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ret = ListNode(0)
        cur = ret
        sum = 0
        
        while l1 or l2 or sum:
            temp = (l1.val if l1 else 0) + (l2.val if l2 else 0) + sum
            sum = temp / 10
            cur.next = ListNode(temp % 10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return ret.next