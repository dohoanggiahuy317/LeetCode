class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg_squares = [num ** 2 for num in nums if num < 0]
        pos_squares = [num ** 2 for num in nums if num >= 0]

        neg_idx = len(neg_squares) - 1
        pos_idx = 0
        squares = []

        for pos_idx, pos_square in enumerate(pos_squares):
            while neg_idx >= 0 and pos_square > neg_squares[neg_idx]:
                squares.append(neg_squares[neg_idx])
                neg_idx -= 1

            squares.append(pos_square)

        return squares
