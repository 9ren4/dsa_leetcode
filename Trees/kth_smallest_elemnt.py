# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        if not root:
            return 0

        queue = deque([root])
        result = []

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        result.sort()
        k = k - 1

        return result[k]
