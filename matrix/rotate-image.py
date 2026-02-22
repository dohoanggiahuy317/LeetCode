class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)

        for i in range((n + 1) // 2):
            for j in range(n // 2):
                coor1 = (i, j)
                coor2 = (j, n - 1 - i)
                coor3 = (n - 1 - i, n - 1 - j)
                coor4 = (n - 1 - j, i)

                val1 = matrix[coor1[0]][coor1[1]]
                val2 = matrix[coor2[0]][coor2[1]]
                val3 = matrix[coor3[0]][coor3[1]]
                val4 = matrix[coor4[0]][coor4[1]]

                matrix[coor1[0]][coor1[1]] = val4
                matrix[coor2[0]][coor2[1]] = val1
                matrix[coor3[0]][coor3[1]] = val2
                matrix[coor4[0]][coor4[1]] = val3
