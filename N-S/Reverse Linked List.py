# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None
        cur=head
        s=[]
        while cur.next!=None:
            s.append(cur.val)
            cur=cur.next
        s.append(cur.val)
        s=s[::-1]
        new=ListNode(0)
        cur2=new
        for x in s:
            cur2.next=ListNode(x)
            cur2=cur2.next
        cur2.next=None
        return new.next
