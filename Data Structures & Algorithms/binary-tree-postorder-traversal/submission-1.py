class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        curr = root
        lastVisited = None

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left

            else:
                peek = stack[-1]

                if peek.right and lastVisited is not peek.right:
                    curr = peek.right
                else:
                    curr = stack.pop()
                    res.append(curr.val)
                    lastVisited = curr
                    curr = None       # ← THIS IS MISSING

        return res