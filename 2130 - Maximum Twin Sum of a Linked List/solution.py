# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1: Find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 3: Calculate the maximum twin sum
        maxVal = 0
        first_half = head
        second_half = prev
        while second_half:  # Iterate through the reversed second half
            maxVal = max(maxVal, first_half.val + second_half.val)
            first_half = first_half.next
            second_half = second_half.next

        return maxVal