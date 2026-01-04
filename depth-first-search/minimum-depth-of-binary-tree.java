/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int minDepth(TreeNode root) {
        if (root == null)
            return 0;
        int ans = minHeight(root, 0, (int)Math.pow(10, 5)+1) + 1;
        return ans;
        
    }
    
    public int minHeight(TreeNode root, int count, int res) {
        if (root == null)
            return res;
        
        if (root.left == null && root.right == null){
            if (res > count)
                res = count;
            return res;
        }
        
        return Math.min(minHeight(root.left, count+1, res), minHeight(root.right, count+1, res));
    }
}