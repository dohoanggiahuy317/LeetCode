class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        ans = [[1], [1, 1]]

        for i in range(numRows - 2):
            new = [1]

            for i in range(len(ans[-1]) - 1):
                new.append(ans[-1][i] + ans[-1][i+1])

            new.append(1)

            ans.append(new)

        return ans
        