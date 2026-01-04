/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null){
            return null;
        }
        ListNode res = new ListNode();
        res.val = head.val;
  
        removeDuplicateRecur(res, head);
        return res;
    }
    
    public ListNode removeDuplicateRecur(ListNode res, ListNode head){
            if (head == null) {
                res = null;
                return res;
            }
            
            if (head.val == res.val)
                removeDuplicateRecur(res, head.next);
                
            if (head.val != res.val){
                ListNode temp = new ListNode(head.val);
                res.next = temp;
                removeDuplicateRecur(res.next, head.next);
            }
            
            return res;
        }
}