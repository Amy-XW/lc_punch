class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stk, benchmark = [], -float('inf')
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            if root.val <= benchmark:
                return False
            benchmark = root.val
            root = root.right
        return True
