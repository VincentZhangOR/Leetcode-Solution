# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head=head
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        cur=self.head
        n=0
        ans=0
        while cur:
            if random.randint(0,n)==0:
                ans=cur.val
            n+=1
            cur=cur.next
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()