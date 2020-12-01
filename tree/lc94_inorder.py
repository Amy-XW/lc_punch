class Solution:
    def inorderTraversal(self, root:TreeNode) -> List[int]:
        if not root: return []
        rslt = self.inorderTraversal(root.left)
        rslt.append(root.val)
        rslt += self.inorderTraversal(root.right)
        return rslt

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stk, rslt = [], []
        while root or stk:
            if root:
                stk.append(root)
                root = root.left
            if not root and stk:
                root = stk.pop()
                rslt.append(root.val)
                root = root.right
        return rslt
        
