# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_of_list = 0
        current = head

        while current:
            len_of_list += 1
            current = current.next

        target = len_of_list - n

        current = head
        index = 1
        if target == 0:
            return head.next
        while current:
            if index == target:
                current.next = current.next.next
            else:
                current = current.next
            index += 1

        return head
