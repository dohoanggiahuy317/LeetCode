class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg_squares = [num ** 2 for num in nums if num < 0]
        pos_squares = [num ** 2 for num in nums if num >= 0]

        neg_idx = len(neg_squares) - 1
        pos_idx = 0
        squares = []

        while neg_idx >= 0 and pos_idx < len(pos_squares):
            while neg_idx >= 0 and pos_squares[pos_idx] > neg_squares[neg_idx]:
                squares.append(neg_squares[neg_idx])
                neg_idx -= 1

            squares.append(pos_squares[pos_idx])
            pos_idx += 1

        return squares
