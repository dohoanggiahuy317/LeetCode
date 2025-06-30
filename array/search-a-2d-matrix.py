class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        def findRow():
            nonlocal matrix, target, m, n
            l, r, ind = 0, m-1, -1
            while l <= r:
                m = (l + r) // 2
                if matrix[m][0] > target:
                    r = m - 1
                else:
                    ind = m
                    l = m + 1
            return ind

        row = findRow()
        if row == -1:
            return False

        l, r = 0, n-1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            if matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False
        
