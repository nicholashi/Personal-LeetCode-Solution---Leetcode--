'''
Theory:

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #Positive, Reversed, List as single node
        #Return Sum with same format

        setDummy = ListNode(0)
        current, carry = setDummy, 0

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            
            #to clear of any addition that is bigger than 10 to bring forward to next node in the list
            carry, val = divmod(val,10) 
            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.next = ListNode(1)

        return setDummy.next



