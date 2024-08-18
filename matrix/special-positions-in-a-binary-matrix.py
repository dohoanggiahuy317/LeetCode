class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        row_sum = list(map(sum, mat))
        
        for i in range(len(mat[0])):
            s_i = 0

            for j in range(len(mat)):
                s_i += mat[j][i]

            for j in range(len(mat)):
                new_s = s_i + row_sum[j]

                if new_s == 2 and mat[j][i] == 1:
                    ans += 1

        return ans