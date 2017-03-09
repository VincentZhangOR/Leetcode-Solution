# coding=utf-8
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        cur = head
        temp = RandomListNode(cur .label)
        dummy = RandomListNode(0)
        dummy.next = temp
        dummy.random = None
        
        d = {}
        
        while cur.next:
            temp.random = None
            d[cur] = temp
            cur = cur.next
            temp.next = RandomListNode (cur.label)
            temp = temp.next
            
        temp.next = None
        temp.random = None
        d[cur] = temp
        
        cur = head
        temp = dummy.next
        while cur:
            if cur.random:
                temp.random = d[cur .random]
            else:
                temp.random = None
            cur = cur.next
            temp = temp.next
        return dummy.next
        
