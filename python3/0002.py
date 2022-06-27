# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        num1a = []
        num2a = []

        while l1:
            num1a.append(l1.val)
            l1 = l1.next

        while l2:
            num2a.append(l2.val)
            l2 = l2.next

        num1 = int(''.join(str(a) for a in reversed(num1a)))
        num2 = int(''.join(str(a) for a in reversed(num2a)))

        outNum = num1 + num2
        outNuma = [int(n) for n in str(outNum)[::-1]]

        head = cur = ListNode()
        for i in outNuma:
            cur.next = ListNode(i)
            cur = cur.next

        return head.next
