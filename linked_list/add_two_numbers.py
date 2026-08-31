# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        p1 = l1
        p2 = l2

        result = []
        carry = 0

        # Keep going while either list still has nodes
        while p1 or p2:

            # If one list has ended, use 0
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0

            summ = val1 + val2 + carry

            # Get the digit
            result.append(summ % 10)

            # Get the carry
            carry = summ // 10

            # Move forward if possible
            if p1:
                p1 = p1.next

            if p2:
                p2 = p2.next

        # If there is a carry left over
        if carry:
            result.append(carry)

        # Convert Python list into linked list
        dummy = ListNode(0)
        current = dummy

        for num in result:
            current.next = ListNode(num)
            current = current.next

        return dummy.next