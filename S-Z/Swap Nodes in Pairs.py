# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return []
        if head.next==None:
            return head
        dummy=ListNode(0)
        dummy.next=head
        cur=dummy
        
        while cur.next and cur.next .next:
            temp=cur.next.next
            cur.next.next=temp.next
            temp.next=cur.next
            cur.next=temp
            cur=cur.next.next
            
            
        return dummy.next
                
