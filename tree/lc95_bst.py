class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n <= 0:
            return None

        def generateBST(low, high):
            if low > high:
                return [None]
            rslt = []
            for i in range(low, high+1):
                left = generateBST(low, i-1)
                right = generateBST(i+1, high)
                for l in left:
                    for r in right:
                        rslt.append(TreeNode(i, l, r))
            return rslt
        return generateBST(1, n)
