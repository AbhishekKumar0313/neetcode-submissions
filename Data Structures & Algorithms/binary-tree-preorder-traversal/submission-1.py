# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        curr=root
        res=[]
        while stack or curr:
            if curr:
                stack.append(curr)
                res.append(curr.val)
                curr=curr.left
            else:
                node=stack.pop()
                curr=node.right
        return res
        