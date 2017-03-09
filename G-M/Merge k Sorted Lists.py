# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h=[]
        for x in lists:
            if x:
                heapq.heappush(h,(x .val,x))
        if h==[]:
            return None
        head=ListNode(0)
        cur=ListNode(0)
        head=cur
        while h!=[]:
            cur.next=heapq.heappop(h )[1]
            cur=cur.next
            if cur.next:
                heapq.heappush(h ,(cur.next.val,cur .next))

