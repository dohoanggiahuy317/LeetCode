class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])

        prev = points[0][:]

        for row in range(1, m):
            left, right = [0] * n, [0] * n

            left[0] = prev[0]
            for i in range(1, n):
                left[i] = max(left[i-1], prev[i] + i)

            right[-1] = prev[-1] - (n-1)
            for i in range(n-2, -1, -1):
                right[i] = max(right[i+1], prev[i] - i)


            for i in range(n):
                prev[i] = points[row][i] + max(left[i] - i, right[i] + i)

        return max(prev)

            