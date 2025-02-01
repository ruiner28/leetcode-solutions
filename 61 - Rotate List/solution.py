# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        length = 1
        cur = head
        while cur.next:
            length += 1
            cur = cur.next
        
        cur.next = head     

        k = k % length
        steps_to_new_tail = length - k
        new_tail = head

        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
        
        # Step 4: Break the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head