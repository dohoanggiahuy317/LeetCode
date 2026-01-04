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
    boolean bool = false;
    
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null)
            return false;
        checkPathSum(root, 0, targetSum);
        return this.bool;
    }
    
    public void checkPathSum(TreeNode root, int leafSum, int target) {
        leafSum += root.val;
            
        if (root.left == null && root.right == null){
            if (leafSum == target) {             
                this.bool = true;
            }
        }
        
        if (root.left != null) {
            checkPathSum(root.left, leafSum, target);
        }
        if (root.right != null) {
            checkPathSum(root.right, leafSum, target);
        }
    }
}
