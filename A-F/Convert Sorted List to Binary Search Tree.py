# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        cur=head
        lst=[]
        while cur!=None:
            lst.append(cur.val)
            cur=cur.next
        return self.help(lst)
        
    def help(self, nums):
        if not nums:
            return None
        left=0
        right=len(nums)-1
        mid=(left+right)/2
        root=TreeNode(nums[mid])
        root.left=self.help(nums[ :mid])
        root.right=self.help (nums[mid+1:])

