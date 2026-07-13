# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # keep track of carry on 
        # recursively add to the next node

        root = ListNode()
        curr = root

        # 123 + 7 
        # 7 + 3, 1 + 2, 1 + 0

        # 99 + 12
        #2 + 9 = 11, 9 + 1 + 1
        carry = 0
        while l1 or l2 or carry != 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            currval = carry + val1 + val2
            remainder = currval % 10
            # 19 % 10 = 9, 19 / 10 = 1
            carry = currval // 10 

            newnode = ListNode(remainder, None)
            curr.next = newnode
            curr = newnode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return root.next

            