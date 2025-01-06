class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
    
'''
This approach gives us a time complexity of O(n) and a space complexity of O(1), where n is the number of nodes in the linked list. Note that this problem can also be solved using hashing, although it would require O(n) space.

The hashing solution: if you continuously iterate using the next pointer, there are two possibilities:

1) If the linked list doesn't have a cycle, you will eventually reach null and finish.
2) If the linked list has a cycle, you will eventually visit a node twice. We can use a set to detect this.
'''    

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
    
#This solution is added for the sake of completeness - the first one is better as it uses less space.    