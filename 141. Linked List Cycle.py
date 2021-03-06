# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            fast = head.next.next
            slow = head.next
            
            while fast != slow:
                fast = fast.next.next
                slow = slow.next
            return True
        except:
            return False