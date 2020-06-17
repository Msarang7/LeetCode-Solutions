# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root.val == val:
            return root
        
        while(root):
            
            if root.val == val:
                return root
            
            if root.val > val :
                root = root.left
            else:
                root = root.right
        return None
            
                