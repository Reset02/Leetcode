/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    // Step 1: Get nodes in sorted order
    void inorderTraversal(TreeNode* node, std::vector<int>& nodes) {
        if (!node) return;
        inorderTraversal(node->left, nodes);
        nodes.push_back(node->val);
        inorderTraversal(node->right, nodes);
    }

    // Step 2: Construct a balanced BST from sorted nodes
    TreeNode* sortedArrayToBST(const std::vector<int>& nums, int start, int end) {
        if (start > end) return nullptr;
        int mid = start + (end - start) / 2;
        TreeNode* root = new TreeNode(nums[mid]);
        root->left = sortedArrayToBST(nums, start, mid - 1);
        root->right = sortedArrayToBST(nums, mid + 1, end);
        return root;
    }
    
    TreeNode* balanceBST(TreeNode* root) {
        std::vector<int> sortedNodes;
        inorderTraversal(root, sortedNodes);
        return sortedArrayToBST(sortedNodes, 0, sortedNodes.size() - 1);
        
    }
};