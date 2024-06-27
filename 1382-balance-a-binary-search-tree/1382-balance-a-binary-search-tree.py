# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Step 1: Get nodes in sorted order
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        sorted_nodes = inorder_traversal(root)
        
        # Step 2: Construct a balanced BST from sorted nodes
        def sorted_array_to_bst(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = sorted_array_to_bst(nums[:mid])
            root.right = sorted_array_to_bst(nums[mid+1:])
            return root
        
        return sorted_array_to_bst(sorted_nodes)
        