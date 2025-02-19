class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = l1 if l1 else l2
        prev = None

#The divmod() method takes two numbers as arguments and returns their quotient and remainder in a tuple.

        while l1 and l2:
            carry, val = divmod(l1.val + l2.val + carry, 10)
            l1.val = val
            prev = l1
            l1 = l1.next
            l2 = l2.next
        if l2:
            prev.next = l2
            l1 = l2   

        while l1 and carry:
            carry, val = divmod(l1.val + carry, 10)
            l1.val = val
            prev = l1
            l1 = l1.next

        if carry:
            prev.next = ListNode(1)
        return head