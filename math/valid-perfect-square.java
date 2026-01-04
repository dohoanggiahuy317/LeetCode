class Solution {
    public boolean isPerfectSquare(int num) {
        int i = 0;
        while (Math.pow(i, 2) < num)
            i += 1;
            
        if (Math.pow(i, 2) == num)
            return true;
        return false;
    }
}