# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in -place instead.
        """
        if head == None:
            return
        slow = head
        fast = head
        while fast.next and fast.next .next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        left = head
        right = mid.next
        if right == None:
            return
        mid.next = None
        cur = right.next
        right.next = None
        while cur:
            temp = cur.next
            cur.next = right
            right = cur
            cur = temp
        dummy = ListNode(0)
        while left or right:
            if left:
                dummy.next = left
                left = left.next
                dummy = dummy.next
            if right:
                dummy.next = right
                right = right.next
                dummy = dummy.next
