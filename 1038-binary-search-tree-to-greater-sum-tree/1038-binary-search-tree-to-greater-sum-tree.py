# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#題目 1038 的 Binary Search Tree to Greater Sum Tree 要求將一個二元搜索樹（BST）轉換為一個 Greater Sum Tree（GST）
#在這個新樹中，每個節點的值將被改變為原樹中所有大於或等於該節點值的節點之和。
#這樣的轉換可以通過一個反向的中序遍歷來完成，這樣我們可以保證節點值的累加順序是從大到小。
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        
        def traverse(node):
            if not node:
                return
            traverse(node.right)
            self.sum += node.val
            node.val = self.sum
            traverse(node.left)
        
        traverse(root)
        return root
        