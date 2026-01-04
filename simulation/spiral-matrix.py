class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def make_spiral(matrix, res = []):
            #base case
            if len(matrix) == 0:
                return res
            if len(matrix) == 1:
                res += matrix[0]
                return res
            
            #first row
            res += matrix[0]
            matrix.pop(0)
            #check if it can continue
            if len(matrix) == 0 or len(matrix[0]) == 0:
                return res
            
            #last column
            for i in range(len(matrix)):             
                res += [matrix[i][-1]]
                matrix[i].pop(-1)
            #check if it can continue
            if len(matrix) == 0 or len(matrix[0]) == 0:
                return res
            
            #last row
            res += matrix[-1][::-1]
            matrix.pop(-1)
            #check if it can continue
            if len(matrix) == 0 or len(matrix[0]) == 0:
                return res
            
            #first column
            for i in range(len(matrix)-1, -1, -1):
                res += [matrix[i][0]]
                matrix[i].pop(0)
            #check if it can continue
            if len(matrix) == 0 or len(matrix[0]) == 0:
                return res
            
            return make_spiral(matrix, res)
            
        return make_spiral(matrix, [])