class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        flat = [board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2]]
        if flat == [0,1,2,3,4,5]:
            return 15
        elif flat == [0,1,2,3,5,4]:
            return -1
        elif flat == [0,1,2,4,3,5]:
            return -1
        elif flat == [0,1,2,4,5,3]:
            return 3
        elif flat == [0,1,2,5,3,4]:
            return 15
        elif flat == [0,1,2,5,4,3]:
            return -1
        elif flat == [0,1,3,2,4,5]:
            return -1
        elif flat == [0,1,3,2,5,4]:
            return 15
        elif flat == [0,1,3,4,2,5]:
            return 3
        elif flat == [0,1,3,4,5,2]:
            return -1
        elif flat == [0,1,3,5,2,4]:
            return -1
        elif flat == [0,1,3,5,4,2]:
            return 17
        elif flat == [0,1,4,2,3,5]:
            return 17
        elif flat == [0,1,4,2,5,3]:
            return -1
        elif flat == [0,1,4,3,2,5]:
            return -1
        elif flat == [0,1,4,3,5,2]:
            return 15
        elif flat == [0,1,4,5,2,3]:
            return 13
        elif flat == [0,1,4,5,3,2]:
            return -1
        elif flat == [0,1,5,2,3,4]:
            return -1
        elif flat == [0,1,5,2,4,3]:
            return 17
        elif flat == [0,1,5,3,2,4]:
            return 13
        elif flat == [0,1,5,3,4,2]:
            return -1
        elif flat == [0,1,5,4,2,3]:
            return -1
        elif flat == [0,1,5,4,3,2]:
            return 7
        elif flat == [0,2,1,3,4,5]:
            return -1
        elif flat == [0,2,1,3,5,4]:
            return 19
        elif flat == [0,2,1,4,3,5]:
            return 15
        elif flat == [0,2,1,4,5,3]:
            return -1
        elif flat == [0,2,1,5,3,4]:
            return -1
        elif flat == [0,2,1,5,4,3]:
            return 13
        elif flat == [0,2,3,1,4,5]:
            return 3
        elif flat == [0,2,3,1,5,4]:
            return -1
        elif flat == [0,2,3,4,1,5]:
            return -1
        elif flat == [0,2,3,4,5,1]:
            return 11
        elif flat == [0,2,3,5,1,4]:
            return 11
        elif flat == [0,2,3,5,4,1]:
            return -1
        elif flat == [0,2,4,1,3,5]:
            return -1
        elif flat == [0,2,4,1,5,3]:
            return 9
        elif flat == [0,2,4,3,1,5]:
            return 15
        elif flat == [0,2,4,3,5,1]:
            return -1
        elif flat == [0,2,4,5,1,3]:
            return -1
        elif flat == [0,2,4,5,3,1]:
            return 15
        elif flat == [0,2,5,1,3,4]:
            return 9
        elif flat == [0,2,5,1,4,3]:
            return -1
        elif flat == [0,2,5,3,1,4]:
            return -1
        elif flat == [0,2,5,3,4,1]:
            return 15
        elif flat == [0,2,5,4,1,3]:
            return 17
        elif flat == [0,2,5,4,3,1]:
            return -1
        elif flat == [0,3,1,2,4,5]:
            return 15
        elif flat == [0,3,1,2,5,4]:
            return -1
        elif flat == [0,3,1,4,2,5]:
            return -1
        elif flat == [0,3,1,4,5,2]:
            return 11
        elif flat == [0,3,1,5,2,4]:
            return 19
        elif flat == [0,3,1,5,4,2]:
            return -1
        elif flat == [0,3,2,1,4,5]:
            return -1
        elif flat == [0,3,2,1,5,4]:
            return 13
        elif flat == [0,3,2,4,1,5]:
            return 17
        elif flat == [0,3,2,4,5,1]:
            return -1
        elif flat == [0,3,2,5,1,4]:
            return -1
        elif flat == [0,3,2,5,4,1]:
            return 19
        elif flat == [0,3,4,1,2,5]:
            return 13
        elif flat == [0,3,4,1,5,2]:
            return -1
        elif flat == [0,3,4,2,1,5]:
            return -1
        elif flat == [0,3,4,2,5,1]:
            return 15
        elif flat == [0,3,4,5,1,2]:
            return 13
        elif flat == [0,3,4,5,2,1]:
            return -1
        elif flat == [0,3,5,1,2,4]:
            return -1
        elif flat == [0,3,5,1,4,2]:
            return 7
        elif flat == [0,3,5,2,1,4]:
            return 9
        elif flat == [0,3,5,2,4,1]:
            return -1
        elif flat == [0,3,5,4,1,2]:
            return -1
        elif flat == [0,3,5,4,2,1]:
            return 11
        elif flat == [0,4,1,2,3,5]:
            return -1
        elif flat == [0,4,1,2,5,3]:
            return 9
        elif flat == [0,4,1,3,2,5]:
            return 13
        elif flat == [0,4,1,3,5,2]:
            return -1
        elif flat == [0,4,1,5,2,3]:
            return -1
        elif flat == [0,4,1,5,3,2]:
            return 9
        elif flat == [0,4,2,1,3,5]:
            return 17
        elif flat == [0,4,2,1,5,3]:
            return -1
        elif flat == [0,4,2,3,1,5]:
            return -1
        elif flat == [0,4,2,3,5,1]:
            return 15
        elif flat == [0,4,2,5,1,3]:
            return 7
        elif flat == [0,4,2,5,3,1]:
            return -1
        elif flat == [0,4,3,1,2,5]:
            return -1
        elif flat == [0,4,3,1,5,2]:
            return 17
        elif flat == [0,4,3,2,1,5]:
            return 7
        elif flat == [0,4,3,2,5,1]:
            return -1
        elif flat == [0,4,3,5,1,2]:
            return -1
        elif flat == [0,4,3,5,2,1]:
            return 11
        elif flat == [0,4,5,1,2,3]:
            return 19
        elif flat == [0,4,5,1,3,2]:
            return -1
        elif flat == [0,4,5,2,1,3]:
            return -1
        elif flat == [0,4,5,2,3,1]:
            return 11
        elif flat == [0,4,5,3,1,2]:
            return 11
        elif flat == [0,4,5,3,2,1]:
            return -1
        elif flat == [0,5,1,2,3,4]:
            return 17
        elif flat == [0,5,1,2,4,3]:
            return -1
        elif flat == [0,5,1,3,2,4]:
            return -1
        elif flat == [0,5,1,3,4,2]:
            return 13
        elif flat == [0,5,1,4,2,3]:
            return 11
        elif flat == [0,5,1,4,3,2]:
            return -1
        elif flat == [0,5,2,1,3,4]:
            return -1
        elif flat == [0,5,2,1,4,3]:
            return 5
        elif flat == [0,5,2,3,1,4]:
            return 13
        elif flat == [0,5,2,3,4,1]:
            return -1
        elif flat == [0,5,2,4,1,3]:
            return -1
        elif flat == [0,5,2,4,3,1]:
            return 15
        elif flat == [0,5,3,1,2,4]:
            return 11
        elif flat == [0,5,3,1,4,2]:
            return -1
        elif flat == [0,5,3,2,1,4]:
            return -1
        elif flat == [0,5,3,2,4,1]:
            return 15
        elif flat == [0,5,3,4,1,2]:
            return 17
        elif flat == [0,5,3,4,2,1]:
            return -1
        elif flat == [0,5,4,1,2,3]:
            return -1
        elif flat == [0,5,4,1,3,2]:
            return 11
        elif flat == [0,5,4,2,1,3]:
            return 11
        elif flat == [0,5,4,2,3,1]:
            return -1
        elif flat == [0,5,4,3,1,2]:
            return -1
        elif flat == [0,5,4,3,2,1]:
            return 15
        elif flat == [1,0,2,3,4,5]:
            return 14
        elif flat == [1,0,2,3,5,4]:
            return -1
        elif flat == [1,0,2,4,3,5]:
            return -1
        elif flat == [1,0,2,4,5,3]:
            return 2
        elif flat == [1,0,2,5,3,4]:
            return 14
        elif flat == [1,0,2,5,4,3]:
            return -1
        elif flat == [1,0,3,2,4,5]:
            return -1
        elif flat == [1,0,3,2,5,4]:
            return 14
        elif flat == [1,0,3,4,2,5]:
            return 2
        elif flat == [1,0,3,4,5,2]:
            return -1
        elif flat == [1,0,3,5,2,4]:
            return -1
        elif flat == [1,0,3,5,4,2]:
            return 16
        elif flat == [1,0,4,2,3,5]:
            return 16
        elif flat == [1,0,4,2,5,3]:
            return -1
        elif flat == [1,0,4,3,2,5]:
            return -1
        elif flat == [1,0,4,3,5,2]:
            return 14
        elif flat == [1,0,4,5,2,3]:
            return 12
        elif flat == [1,0,4,5,3,2]:
            return -1
        elif flat == [1,0,5,2,3,4]:
            return -1
        elif flat == [1,0,5,2,4,3]:
            return 16
        elif flat == [1,0,5,3,2,4]:
            return 12
        elif flat == [1,0,5,3,4,2]:
            return -1
        elif flat == [1,0,5,4,2,3]:
            return -1
        elif flat == [1,0,5,4,3,2]:
            return 6
        elif flat == [1,2,0,3,4,5]:
            return 13
        elif flat == [1,2,0,3,5,4]:
            return -1
        elif flat == [1,2,0,4,3,5]:
            return -1
        elif flat == [1,2,0,4,5,3]:
            return 1
        elif flat == [1,2,0,5,3,4]:
            return 13
        elif flat == [1,2,0,5,4,3]:
            return -1
        elif flat == [1,2,3,0,4,5]:
            return 2
        elif flat == [1,2,3,0,5,4]:
            return -1
        elif flat == [1,2,3,4,0,5]:
            return 1
        elif flat == [1,2,3,4,5,0]:
            return 0
        elif flat == [1,2,3,5,0,4]:
            return -1
        elif flat == [1,2,3,5,4,0]:
            return -1
        elif flat == [1,2,4,0,3,5]:
            return -1
        elif flat == [1,2,4,0,5,3]:
            return 10
        elif flat == [1,2,4,3,0,5]:
            return -1
        elif flat == [1,2,4,3,5,0]:
            return -1
        elif flat == [1,2,4,5,0,3]:
            return 11
        elif flat == [1,2,4,5,3,0]:
            return 12
        elif flat == [1,2,5,0,3,4]:
            return 10
        elif flat == [1,2,5,0,4,3]:
            return -1
        elif flat == [1,2,5,3,0,4]:
            return 11
        elif flat == [1,2,5,3,4,0]:
            return 12
        elif flat == [1,2,5,4,0,3]:
            return -1
        elif flat == [1,2,5,4,3,0]:
            return -1
        elif flat == [1,3,0,2,4,5]:
            return -1
        elif flat == [1,3,0,2,5,4]:
            return 15
        elif flat == [1,3,0,4,2,5]:
            return 3
        elif flat == [1,3,0,4,5,2]:
            return -1
        elif flat == [1,3,0,5,2,4]:
            return -1
        elif flat == [1,3,0,5,4,2]:
            return 17
        elif flat == [1,3,2,0,4,5]:
            return -1
        elif flat == [1,3,2,0,5,4]:
            return 14
        elif flat == [1,3,2,4,0,5]:
            return -1
        elif flat == [1,3,2,4,5,0]:
            return -1
        elif flat == [1,3,2,5,0,4]:
            return 15
        elif flat == [1,3,2,5,4,0]:
            return 16
        elif flat == [1,3,4,0,2,5]:
            return 14
        elif flat == [1,3,4,0,5,2]:
            return -1
        elif flat == [1,3,4,2,0,5]:
            return 15
        elif flat == [1,3,4,2,5,0]:
            return 16
        elif flat == [1,3,4,5,0,2]:
            return -1
        elif flat == [1,3,4,5,2,0]:
            return -1
        elif flat == [1,3,5,0,2,4]:
            return -1
        elif flat == [1,3,5,0,4,2]:
            return 6
        elif flat == [1,3,5,2,0,4]:
            return -1
        elif flat == [1,3,5,2,4,0]:
            return -1
        elif flat == [1,3,5,4,0,2]:
            return 5
        elif flat == [1,3,5,4,2,0]:
            return 4
        elif flat == [1,4,0,2,3,5]:
            return 17
        elif flat == [1,4,0,2,5,3]:
            return -1
        elif flat == [1,4,0,3,2,5]:
            return -1
        elif flat == [1,4,0,3,5,2]:
            return 15
        elif flat == [1,4,0,5,2,3]:
            return 13
        elif flat == [1,4,0,5,3,2]:
            return -1
        elif flat == [1,4,2,0,3,5]:
            return 16
        elif flat == [1,4,2,0,5,3]:
            return -1
        elif flat == [1,4,2,3,0,5]:
            return 15
        elif flat == [1,4,2,3,5,0]:
            return 16
        elif flat == [1,4,2,5,0,3]:
            return -1
        elif flat == [1,4,2,5,3,0]:
            return -1
        elif flat == [1,4,3,0,2,5]:
            return -1
        elif flat == [1,4,3,0,5,2]:
            return 16
        elif flat == [1,4,3,2,0,5]:
            return -1
        elif flat == [1,4,3,2,5,0]:
            return -1
        elif flat == [1,4,3,5,0,2]:
            return 15
        elif flat == [1,4,3,5,2,0]:
            return 14
        elif flat == [1,4,5,0,2,3]:
            return 18
        elif flat == [1,4,5,0,3,2]:
            return -1
        elif flat == [1,4,5,2,0,3]:
            return 17
        elif flat == [1,4,5,2,3,0]:
            return 18
        elif flat == [1,4,5,3,0,2]:
            return -1
        elif flat == [1,4,5,3,2,0]:
            return -1
        elif flat == [1,5,0,2,3,4]:
            return -1
        elif flat == [1,5,0,2,4,3]:
            return 15
        elif flat == [1,5,0,3,2,4]:
            return 13
        elif flat == [1,5,0,3,4,2]:
            return -1
        elif flat == [1,5,0,4,2,3]:
            return -1
        elif flat == [1,5,0,4,3,2]:
            return 5
        elif flat == [1,5,2,0,3,4]:
            return -1
        elif flat == [1,5,2,0,4,3]:
            return 4
        elif flat == [1,5,2,3,0,4]:
            return -1
        elif flat == [1,5,2,3,4,0]:
            return -1
        elif flat == [1,5,2,4,0,3]:
            return 3
        elif flat == [1,5,2,4,3,0]:
            return 4
        elif flat == [1,5,3,0,2,4]:
            return 12
        elif flat == [1,5,3,0,4,2]:
            return -1
        elif flat == [1,5,3,2,0,4]:
            return 13
        elif flat == [1,5,3,2,4,0]:
            return 14
        elif flat == [1,5,3,4,0,2]:
            return -1
        elif flat == [1,5,3,4,2,0]:
            return -1
        elif flat == [1,5,4,0,2,3]:
            return -1
        elif flat == [1,5,4,0,3,2]:
            return 12
        elif flat == [1,5,4,2,0,3]:
            return -1
        elif flat == [1,5,4,2,3,0]:
            return -1
        elif flat == [1,5,4,3,0,2]:
            return 13
        elif flat == [1,5,4,3,2,0]:
            return 14
        elif flat == [2,0,1,3,4,5]:
            return -1
        elif flat == [2,0,1,3,5,4]:
            return 18
        elif flat == [2,0,1,4,3,5]:
            return 16
        elif flat == [2,0,1,4,5,3]:
            return -1
        elif flat == [2,0,1,5,3,4]:
            return -1
        elif flat == [2,0,1,5,4,3]:
            return 12
        elif flat == [2,0,3,1,4,5]:
            return 4
        elif flat == [2,0,3,1,5,4]:
            return -1
        elif flat == [2,0,3,4,1,5]:
            return -1
        elif flat == [2,0,3,4,5,1]:
            return 12
        elif flat == [2,0,3,5,1,4]:
            return 12
        elif flat == [2,0,3,5,4,1]:
            return -1
        elif flat == [2,0,4,1,3,5]:
            return -1
        elif flat == [2,0,4,1,5,3]:
            return 8
        elif flat == [2,0,4,3,1,5]:
            return 16
        elif flat == [2,0,4,3,5,1]:
            return -1
        elif flat == [2,0,4,5,1,3]:
            return -1
        elif flat == [2,0,4,5,3,1]:
            return 14
        elif flat == [2,0,5,1,3,4]:
            return 8
        elif flat == [2,0,5,1,4,3]:
            return -1
        elif flat == [2,0,5,3,1,4]:
            return -1
        elif flat == [2,0,5,3,4,1]:
            return 14
        elif flat == [2,0,5,4,1,3]:
            return 16
        elif flat == [2,0,5,4,3,1]:
            return -1
        elif flat == [2,1,0,3,4,5]:
            return -1
        elif flat == [2,1,0,3,5,4]:
            return 19
        elif flat == [2,1,0,4,3,5]:
            return 17
        elif flat == [2,1,0,4,5,3]:
            return -1
        elif flat == [2,1,0,5,3,4]:
            return -1
        elif flat == [2,1,0,5,4,3]:
            return 13
        elif flat == [2,1,3,0,4,5]:
            return -1
        elif flat == [2,1,3,0,5,4]:
            return 14
        elif flat == [2,1,3,4,0,5]:
            return -1
        elif flat == [2,1,3,4,5,0]:
            return -1
        elif flat == [2,1,3,5,0,4]:
            return 13
        elif flat == [2,1,3,5,4,0]:
            return 14
        elif flat == [2,1,4,0,3,5]:
            return 18
        elif flat == [2,1,4,0,5,3]:
            return -1
        elif flat == [2,1,4,3,0,5]:
            return 17
        elif flat == [2,1,4,3,5,0]:
            return 18
        elif flat == [2,1,4,5,0,3]:
            return -1
        elif flat == [2,1,4,5,3,0]:
            return -1
        elif flat == [2,1,5,0,3,4]:
            return -1
        elif flat == [2,1,5,0,4,3]:
            return 18
        elif flat == [2,1,5,3,0,4]:
            return -1
        elif flat == [2,1,5,3,4,0]:
            return -1
        elif flat == [2,1,5,4,0,3]:
            return 17
        elif flat == [2,1,5,4,3,0]:
            return 18
        elif flat == [2,3,0,1,4,5]:
            return 5
        elif flat == [2,3,0,1,5,4]:
            return -1
        elif flat == [2,3,0,4,1,5]:
            return -1
        elif flat == [2,3,0,4,5,1]:
            return 13
        elif flat == [2,3,0,5,1,4]:
            return 13
        elif flat == [2,3,0,5,4,1]:
            return -1
        elif flat == [2,3,1,0,4,5]:
            return 16
        elif flat == [2,3,1,0,5,4]:
            return -1
        elif flat == [2,3,1,4,0,5]:
            return 15
        elif flat == [2,3,1,4,5,0]:
            return 14
        elif flat == [2,3,1,5,0,4]:
            return -1
        elif flat == [2,3,1,5,4,0]:
            return -1
        elif flat == [2,3,4,0,1,5]:
            return -1
        elif flat == [2,3,4,0,5,1]:
            return 16
        elif flat == [2,3,4,1,0,5]:
            return -1
        elif flat == [2,3,4,1,5,0]:
            return -1
        elif flat == [2,3,4,5,0,1]:
            return 15
        elif flat == [2,3,4,5,1,0]:
            return 14
        elif flat == [2,3,5,0,1,4]:
            return 8
        elif flat == [2,3,5,0,4,1]:
            return -1
        elif flat == [2,3,5,1,0,4]:
            return 7
        elif flat == [2,3,5,1,4,0]:
            return 6
        elif flat == [2,3,5,4,0,1]:
            return -1
        elif flat == [2,3,5,4,1,0]:
            return -1
        elif flat == [2,4,0,1,3,5]:
            return -1
        elif flat == [2,4,0,1,5,3]:
            return 7
        elif flat == [2,4,0,3,1,5]:
            return 15
        elif flat == [2,4,0,3,5,1]:
            return -1
        elif flat == [2,4,0,5,1,3]:
            return -1
        elif flat == [2,4,0,5,3,1]:
            return 13
        elif flat == [2,4,1,0,3,5]:
            return -1
        elif flat == [2,4,1,0,5,3]:
            return 10
        elif flat == [2,4,1,3,0,5]:
            return -1
        elif flat == [2,4,1,3,5,0]:
            return -1
        elif flat == [2,4,1,5,0,3]:
            return 11
        elif flat == [2,4,1,5,3,0]:
            return 12
        elif flat == [2,4,3,0,1,5]:
            return 6
        elif flat == [2,4,3,0,5,1]:
            return -1
        elif flat == [2,4,3,1,0,5]:
            return 5
        elif flat == [2,4,3,1,5,0]:
            return 6
        elif flat == [2,4,3,5,0,1]:
            return -1
        elif flat == [2,4,3,5,1,0]:
            return -1
        elif flat == [2,4,5,0,1,3]:
            return -1
        elif flat == [2,4,5,0,3,1]:
            return 12
        elif flat == [2,4,5,1,0,3]:
            return -1
        elif flat == [2,4,5,1,3,0]:
            return -1
        elif flat == [2,4,5,3,0,1]:
            return 13
        elif flat == [2,4,5,3,1,0]:
            return 14
        elif flat == [2,5,0,1,3,4]:
            return 9
        elif flat == [2,5,0,1,4,3]:
            return -1
        elif flat == [2,5,0,3,1,4]:
            return -1
        elif flat == [2,5,0,3,4,1]:
            return 15
        elif flat == [2,5,0,4,1,3]:
            return 15
        elif flat == [2,5,0,4,3,1]:
            return -1
        elif flat == [2,5,1,0,3,4]:
            return 18
        elif flat == [2,5,1,0,4,3]:
            return -1
        elif flat == [2,5,1,3,0,4]:
            return 17
        elif flat == [2,5,1,3,4,0]:
            return 16
        elif flat == [2,5,1,4,0,3]:
            return -1
        elif flat == [2,5,1,4,3,0]:
            return -1
        elif flat == [2,5,3,0,1,4]:
            return -1
        elif flat == [2,5,3,0,4,1]:
            return 14
        elif flat == [2,5,3,1,0,4]:
            return -1
        elif flat == [2,5,3,1,4,0]:
            return -1
        elif flat == [2,5,3,4,0,1]:
            return 13
        elif flat == [2,5,3,4,1,0]:
            return 14
        elif flat == [2,5,4,0,1,3]:
            return 10
        elif flat == [2,5,4,0,3,1]:
            return -1
        elif flat == [2,5,4,1,0,3]:
            return 9
        elif flat == [2,5,4,1,3,0]:
            return 10
        elif flat == [2,5,4,3,0,1]:
            return -1
        elif flat == [2,5,4,3,1,0]:
            return -1
        elif flat == [3,0,1,2,4,5]:
            return 14
        elif flat == [3,0,1,2,5,4]:
            return -1
        elif flat == [3,0,1,4,2,5]:
            return -1
        elif flat == [3,0,1,4,5,2]:
            return 12
        elif flat == [3,0,1,5,2,4]:
            return 18
        elif flat == [3,0,1,5,4,2]:
            return -1
        elif flat == [3,0,2,1,4,5]:
            return -1
        elif flat == [3,0,2,1,5,4]:
            return 12
        elif flat == [3,0,2,4,1,5]:
            return 16
        elif flat == [3,0,2,4,5,1]:
            return -1
        elif flat == [3,0,2,5,1,4]:
            return -1
        elif flat == [3,0,2,5,4,1]:
            return 18
        elif flat == [3,0,4,1,2,5]:
            return 12
        elif flat == [3,0,4,1,5,2]:
            return -1
        elif flat == [3,0,4,2,1,5]:
            return -1
        elif flat == [3,0,4,2,5,1]:
            return 14
        elif flat == [3,0,4,5,1,2]:
            return 14
        elif flat == [3,0,4,5,2,1]:
            return -1
        elif flat == [3,0,5,1,2,4]:
            return -1
        elif flat == [3,0,5,1,4,2]:
            return 8
        elif flat == [3,0,5,2,1,4]:
            return 10
        elif flat == [3,0,5,2,4,1]:
            return -1
        elif flat == [3,0,5,4,1,2]:
            return -1
        elif flat == [3,0,5,4,2,1]:
            return 12
        elif flat == [3,1,0,2,4,5]:
            return 13
        elif flat == [3,1,0,2,5,4]:
            return -1
        elif flat == [3,1,0,4,2,5]:
            return -1
        elif flat == [3,1,0,4,5,2]:
            return 13
        elif flat == [3,1,0,5,2,4]:
            return 17
        elif flat == [3,1,0,5,4,2]:
            return -1
        elif flat == [3,1,2,0,4,5]:
            return 16
        elif flat == [3,1,2,0,5,4]:
            return -1
        elif flat == [3,1,2,4,0,5]:
            return 15
        elif flat == [3,1,2,4,5,0]:
            return 14
        elif flat == [3,1,2,5,0,4]:
            return -1
        elif flat == [3,1,2,5,4,0]:
            return -1
        elif flat == [3,1,4,0,2,5]:
            return -1
        elif flat == [3,1,4,0,5,2]:
            return 16
        elif flat == [3,1,4,2,0,5]:
            return -1
        elif flat == [3,1,4,2,5,0]:
            return -1
        elif flat == [3,1,4,5,0,2]:
            return 15
        elif flat == [3,1,4,5,2,0]:
            return 16
        elif flat == [3,1,5,0,2,4]:
            return 12
        elif flat == [3,1,5,0,4,2]:
            return -1
        elif flat == [3,1,5,2,0,4]:
            return 11
        elif flat == [3,1,5,2,4,0]:
            return 12
        elif flat == [3,1,5,4,0,2]:
            return -1
        elif flat == [3,1,5,4,2,0]:
            return -1
        elif flat == [3,2,0,1,4,5]:
            return -1
        elif flat == [3,2,0,1,5,4]:
            return 13
        elif flat == [3,2,0,4,1,5]:
            return 15
        elif flat == [3,2,0,4,5,1]:
            return -1
        elif flat == [3,2,0,5,1,4]:
            return -1
        elif flat == [3,2,0,5,4,1]:
            return 19
        elif flat == [3,2,1,0,4,5]:
            return -1
        elif flat == [3,2,1,0,5,4]:
            return 20
        elif flat == [3,2,1,4,0,5]:
            return -1
        elif flat == [3,2,1,4,5,0]:
            return -1
        elif flat == [3,2,1,5,0,4]:
            return 19
        elif flat == [3,2,1,5,4,0]:
            return 20
        elif flat == [3,2,4,0,1,5]:
            return 14
        elif flat == [3,2,4,0,5,1]:
            return -1
        elif flat == [3,2,4,1,0,5]:
            return 13
        elif flat == [3,2,4,1,5,0]:
            return 14
        elif flat == [3,2,4,5,0,1]:
            return -1
        elif flat == [3,2,4,5,1,0]:
            return -1
        elif flat == [3,2,5,0,1,4]:
            return -1
        elif flat == [3,2,5,0,4,1]:
            return 14
        elif flat == [3,2,5,1,0,4]:
            return -1
        elif flat == [3,2,5,1,4,0]:
            return -1
        elif flat == [3,2,5,4,0,1]:
            return 13
        elif flat == [3,2,5,4,1,0]:
            return 14
        elif flat == [3,4,0,1,2,5]:
            return 11
        elif flat == [3,4,0,1,5,2]:
            return -1
        elif flat == [3,4,0,2,1,5]:
            return -1
        elif flat == [3,4,0,2,5,1]:
            return 15
        elif flat == [3,4,0,5,1,2]:
            return 15
        elif flat == [3,4,0,5,2,1]:
            return -1
        elif flat == [3,4,1,0,2,5]:
            return 14
        elif flat == [3,4,1,0,5,2]:
            return -1
        elif flat == [3,4,1,2,0,5]:
            return 15
        elif flat == [3,4,1,2,5,0]:
            return 16
        elif flat == [3,4,1,5,0,2]:
            return -1
        elif flat == [3,4,1,5,2,0]:
            return -1
        elif flat == [3,4,2,0,1,5]:
            return -1
        elif flat == [3,4,2,0,5,1]:
            return 16
        elif flat == [3,4,2,1,0,5]:
            return -1
        elif flat == [3,4,2,1,5,0]:
            return -1
        elif flat == [3,4,2,5,0,1]:
            return 17
        elif flat == [3,4,2,5,1,0]:
            return 16
        elif flat == [3,4,5,0,1,2]:
            return 10
        elif flat == [3,4,5,0,2,1]:
            return -1
        elif flat == [3,4,5,1,0,2]:
            return 9
        elif flat == [3,4,5,1,2,0]:
            return 10
        elif flat == [3,4,5,2,0,1]:
            return -1
        elif flat == [3,4,5,2,1,0]:
            return -1
        elif flat == [3,5,0,1,2,4]:
            return -1
        elif flat == [3,5,0,1,4,2]:
            return 9
        elif flat == [3,5,0,2,1,4]:
            return 11
        elif flat == [3,5,0,2,4,1]:
            return -1
        elif flat == [3,5,0,4,1,2]:
            return -1
        elif flat == [3,5,0,4,2,1]:
            return 13
        elif flat == [3,5,1,0,2,4]:
            return -1
        elif flat == [3,5,1,0,4,2]:
            return 14
        elif flat == [3,5,1,2,0,4]:
            return -1
        elif flat == [3,5,1,2,4,0]:
            return -1
        elif flat == [3,5,1,4,0,2]:
            return 13
        elif flat == [3,5,1,4,2,0]:
            return 14
        elif flat == [3,5,2,0,1,4]:
            return 12
        elif flat == [3,5,2,0,4,1]:
            return -1
        elif flat == [3,5,2,1,0,4]:
            return 11
        elif flat == [3,5,2,1,4,0]:
            return 10
        elif flat == [3,5,2,4,0,1]:
            return -1
        elif flat == [3,5,2,4,1,0]:
            return -1
        elif flat == [3,5,4,0,1,2]:
            return -1
        elif flat == [3,5,4,0,2,1]:
            return 14
        elif flat == [3,5,4,1,0,2]:
            return -1
        elif flat == [3,5,4,1,2,0]:
            return -1
        elif flat == [3,5,4,2,0,1]:
            return 13
        elif flat == [3,5,4,2,1,0]:
            return 12
        elif flat == [4,0,1,2,3,5]:
            return -1
        elif flat == [4,0,1,2,5,3]:
            return 8
        elif flat == [4,0,1,3,2,5]:
            return 12
        elif flat == [4,0,1,3,5,2]:
            return -1
        elif flat == [4,0,1,5,2,3]:
            return -1
        elif flat == [4,0,1,5,3,2]:
            return 8
        elif flat == [4,0,2,1,3,5]:
            return 18
        elif flat == [4,0,2,1,5,3]:
            return -1
        elif flat == [4,0,2,3,1,5]:
            return -1
        elif flat == [4,0,2,3,5,1]:
            return 14
        elif flat == [4,0,2,5,1,3]:
            return 6
        elif flat == [4,0,2,5,3,1]:
            return -1
        elif flat == [4,0,3,1,2,5]:
            return -1
        elif flat == [4,0,3,1,5,2]:
            return 18
        elif flat == [4,0,3,2,1,5]:
            return 6
        elif flat == [4,0,3,2,5,1]:
            return -1
        elif flat == [4,0,3,5,1,2]:
            return -1
        elif flat == [4,0,3,5,2,1]:
            return 10
        elif flat == [4,0,5,1,2,3]:
            return 20
        elif flat == [4,0,5,1,3,2]:
            return -1
        elif flat == [4,0,5,2,1,3]:
            return -1
        elif flat == [4,0,5,2,3,1]:
            return 10
        elif flat == [4,0,5,3,1,2]:
            return 10
        elif flat == [4,0,5,3,2,1]:
            return -1
        elif flat == [4,1,0,2,3,5]:
            return -1
        elif flat == [4,1,0,2,5,3]:
            return 7
        elif flat == [4,1,0,3,2,5]:
            return 11
        elif flat == [4,1,0,3,5,2]:
            return -1
        elif flat == [4,1,0,5,2,3]:
            return -1
        elif flat == [4,1,0,5,3,2]:
            return 7
        elif flat == [4,1,2,0,3,5]:
            return -1
        elif flat == [4,1,2,0,5,3]:
            return 4
        elif flat == [4,1,2,3,0,5]:
            return -1
        elif flat == [4,1,2,3,5,0]:
            return -1
        elif flat == [4,1,2,5,0,3]:
            return 5
        elif flat == [4,1,2,5,3,0]:
            return 6
        elif flat == [4,1,3,0,2,5]:
            return 4
        elif flat == [4,1,3,0,5,2]:
            return -1
        elif flat == [4,1,3,2,0,5]:
            return 5
        elif flat == [4,1,3,2,5,0]:
            return 6
        elif flat == [4,1,3,5,0,2]:
            return -1
        elif flat == [4,1,3,5,2,0]:
            return -1
        elif flat == [4,1,5,0,2,3]:
            return -1
        elif flat == [4,1,5,0,3,2]:
            return 8
        elif flat == [4,1,5,2,0,3]:
            return -1
        elif flat == [4,1,5,2,3,0]:
            return -1
        elif flat == [4,1,5,3,0,2]:
            return 9
        elif flat == [4,1,5,3,2,0]:
            return 10
        elif flat == [4,2,0,1,3,5]:
            return 19
        elif flat == [4,2,0,1,5,3]:
            return -1
        elif flat == [4,2,0,3,1,5]:
            return -1
        elif flat == [4,2,0,3,5,1]:
            return 15
        elif flat == [4,2,0,5,1,3]:
            return 7
        elif flat == [4,2,0,5,3,1]:
            return -1
        elif flat == [4,2,1,0,3,5]:
            return 14
        elif flat == [4,2,1,0,5,3]:
            return -1
        elif flat == [4,2,1,3,0,5]:
            return 13
        elif flat == [4,2,1,3,5,0]:
            return 14
        elif flat == [4,2,1,5,0,3]:
            return -1
        elif flat == [4,2,1,5,3,0]:
            return -1
        elif flat == [4,2,3,0,1,5]:
            return -1
        elif flat == [4,2,3,0,5,1]:
            return 10
        elif flat == [4,2,3,1,0,5]:
            return -1
        elif flat == [4,2,3,1,5,0]:
            return -1
        elif flat == [4,2,3,5,0,1]:
            return 9
        elif flat == [4,2,3,5,1,0]:
            return 8
        elif flat == [4,2,5,0,1,3]:
            return 18
        elif flat == [4,2,5,0,3,1]:
            return -1
        elif flat == [4,2,5,1,0,3]:
            return 19
        elif flat == [4,2,5,1,3,0]:
            return 20
        elif flat == [4,2,5,3,0,1]:
            return -1
        elif flat == [4,2,5,3,1,0]:
            return -1
        elif flat == [4,3,0,1,2,5]:
            return -1
        elif flat == [4,3,0,1,5,2]:
            return 19
        elif flat == [4,3,0,2,1,5]:
            return 7
        elif flat == [4,3,0,2,5,1]:
            return -1
        elif flat == [4,3,0,5,1,2]:
            return -1
        elif flat == [4,3,0,5,2,1]:
            return 11
        elif flat == [4,3,1,0,2,5]:
            return -1
        elif flat == [4,3,1,0,5,2]:
            return 10
        elif flat == [4,3,1,2,0,5]:
            return -1
        elif flat == [4,3,1,2,5,0]:
            return -1
        elif flat == [4,3,1,5,0,2]:
            return 9
        elif flat == [4,3,1,5,2,0]:
            return 10
        elif flat == [4,3,2,0,1,5]:
            return 18
        elif flat == [4,3,2,0,5,1]:
            return -1
        elif flat == [4,3,2,1,0,5]:
            return 19
        elif flat == [4,3,2,1,5,0]:
            return 20
        elif flat == [4,3,2,5,0,1]:
            return -1
        elif flat == [4,3,2,5,1,0]:
            return -1
        elif flat == [4,3,5,0,1,2]:
            return -1
        elif flat == [4,3,5,0,2,1]:
            return 10
        elif flat == [4,3,5,1,0,2]:
            return -1
        elif flat == [4,3,5,1,2,0]:
            return -1
        elif flat == [4,3,5,2,0,1]:
            return 9
        elif flat == [4,3,5,2,1,0]:
            return 8
        elif flat == [4,5,0,1,2,3]:
            return 21
        elif flat == [4,5,0,1,3,2]:
            return -1
        elif flat == [4,5,0,2,1,3]:
            return -1
        elif flat == [4,5,0,2,3,1]:
            return 11
        elif flat == [4,5,0,3,1,2]:
            return 11
        elif flat == [4,5,0,3,2,1]:
            return -1
        elif flat == [4,5,1,0,2,3]:
            return 10
        elif flat == [4,5,1,0,3,2]:
            return -1
        elif flat == [4,5,1,2,0,3]:
            return 9
        elif flat == [4,5,1,2,3,0]:
            return 10
        elif flat == [4,5,1,3,0,2]:
            return -1
        elif flat == [4,5,1,3,2,0]:
            return -1
        elif flat == [4,5,2,0,1,3]:
            return -1
        elif flat == [4,5,2,0,3,1]:
            return 14
        elif flat == [4,5,2,1,0,3]:
            return -1
        elif flat == [4,5,2,1,3,0]:
            return -1
        elif flat == [4,5,2,3,0,1]:
            return 13
        elif flat == [4,5,2,3,1,0]:
            return 12
        elif flat == [4,5,3,0,1,2]:
            return 18
        elif flat == [4,5,3,0,2,1]:
            return -1
        elif flat == [4,5,3,1,0,2]:
            return 19
        elif flat == [4,5,3,1,2,0]:
            return 20
        elif flat == [4,5,3,2,0,1]:
            return -1
        elif flat == [4,5,3,2,1,0]:
            return -1
        elif flat == [5,0,1,2,3,4]:
            return 16
        elif flat == [5,0,1,2,4,3]:
            return -1
        elif flat == [5,0,1,3,2,4]:
            return -1
        elif flat == [5,0,1,3,4,2]:
            return 12
        elif flat == [5,0,1,4,2,3]:
            return 12
        elif flat == [5,0,1,4,3,2]:
            return -1
        elif flat == [5,0,2,1,3,4]:
            return -1
        elif flat == [5,0,2,1,4,3]:
            return 6
        elif flat == [5,0,2,3,1,4]:
            return 14
        elif flat == [5,0,2,3,4,1]:
            return -1
        elif flat == [5,0,2,4,1,3]:
            return -1
        elif flat == [5,0,2,4,3,1]:
            return 16
        elif flat == [5,0,3,1,2,4]:
            return 10
        elif flat == [5,0,3,1,4,2]:
            return -1
        elif flat == [5,0,3,2,1,4]:
            return -1
        elif flat == [5,0,3,2,4,1]:
            return 14
        elif flat == [5,0,3,4,1,2]:
            return 16
        elif flat == [5,0,3,4,2,1]:
            return -1
        elif flat == [5,0,4,1,2,3]:
            return -1
        elif flat == [5,0,4,1,3,2]:
            return 10
        elif flat == [5,0,4,2,1,3]:
            return 12
        elif flat == [5,0,4,2,3,1]:
            return -1
        elif flat == [5,0,4,3,1,2]:
            return -1
        elif flat == [5,0,4,3,2,1]:
            return 14
        elif flat == [5,1,0,2,3,4]:
            return 15
        elif flat == [5,1,0,2,4,3]:
            return -1
        elif flat == [5,1,0,3,2,4]:
            return -1
        elif flat == [5,1,0,3,4,2]:
            return 13
        elif flat == [5,1,0,4,2,3]:
            return 13
        elif flat == [5,1,0,4,3,2]:
            return -1
        elif flat == [5,1,2,0,3,4]:
            return 16
        elif flat == [5,1,2,0,4,3]:
            return -1
        elif flat == [5,1,2,3,0,4]:
            return 15
        elif flat == [5,1,2,3,4,0]:
            return 14
        elif flat == [5,1,2,4,0,3]:
            return -1
        elif flat == [5,1,2,4,3,0]:
            return -1
        elif flat == [5,1,3,0,2,4]:
            return -1
        elif flat == [5,1,3,0,4,2]:
            return 16
        elif flat == [5,1,3,2,0,4]:
            return -1
        elif flat == [5,1,3,2,4,0]:
            return -1
        elif flat == [5,1,3,4,0,2]:
            return 15
        elif flat == [5,1,3,4,2,0]:
            return 14
        elif flat == [5,1,4,0,2,3]:
            return 14
        elif flat == [5,1,4,0,3,2]:
            return -1
        elif flat == [5,1,4,2,0,3]:
            return 13
        elif flat == [5,1,4,2,3,0]:
            return 14
        elif flat == [5,1,4,3,0,2]:
            return -1
        elif flat == [5,1,4,3,2,0]:
            return -1
        elif flat == [5,2,0,1,3,4]:
            return -1
        elif flat == [5,2,0,1,4,3]:
            return 7
        elif flat == [5,2,0,3,1,4]:
            return 15
        elif flat == [5,2,0,3,4,1]:
            return -1
        elif flat == [5,2,0,4,1,3]:
            return -1
        elif flat == [5,2,0,4,3,1]:
            return 15
        elif flat == [5,2,1,0,3,4]:
            return -1
        elif flat == [5,2,1,0,4,3]:
            return 14
        elif flat == [5,2,1,3,0,4]:
            return -1
        elif flat == [5,2,1,3,4,0]:
            return -1
        elif flat == [5,2,1,4,0,3]:
            return 13
        elif flat == [5,2,1,4,3,0]:
            return 14
        elif flat == [5,2,3,0,1,4]:
            return 10
        elif flat == [5,2,3,0,4,1]:
            return -1
        elif flat == [5,2,3,1,0,4]:
            return 9
        elif flat == [5,2,3,1,4,0]:
            return 8
        elif flat == [5,2,3,4,0,1]:
            return -1
        elif flat == [5,2,3,4,1,0]:
            return -1
        elif flat == [5,2,4,0,1,3]:
            return -1
        elif flat == [5,2,4,0,3,1]:
            return 16
        elif flat == [5,2,4,1,0,3]:
            return -1
        elif flat == [5,2,4,1,3,0]:
            return -1
        elif flat == [5,2,4,3,0,1]:
            return 15
        elif flat == [5,2,4,3,1,0]:
            return 16
        elif flat == [5,3,0,1,2,4]:
            return 11
        elif flat == [5,3,0,1,4,2]:
            return -1
        elif flat == [5,3,0,2,1,4]:
            return -1
        elif flat == [5,3,0,2,4,1]:
            return 15
        elif flat == [5,3,0,4,1,2]:
            return 17
        elif flat == [5,3,0,4,2,1]:
            return -1
        elif flat == [5,3,1,0,2,4]:
            return 18
        elif flat == [5,3,1,0,4,2]:
            return -1
        elif flat == [5,3,1,2,0,4]:
            return 17
        elif flat == [5,3,1,2,4,0]:
            return 16
        elif flat == [5,3,1,4,0,2]:
            return -1
        elif flat == [5,3,1,4,2,0]:
            return -1
        elif flat == [5,3,2,0,1,4]:
            return -1
        elif flat == [5,3,2,0,4,1]:
            return 18
        elif flat == [5,3,2,1,0,4]:
            return -1
        elif flat == [5,3,2,1,4,0]:
            return -1
        elif flat == [5,3,2,4,0,1]:
            return 17
        elif flat == [5,3,2,4,1,0]:
            return 18
        elif flat == [5,3,4,0,1,2]:
            return 12
        elif flat == [5,3,4,0,2,1]:
            return -1
        elif flat == [5,3,4,1,0,2]:
            return 11
        elif flat == [5,3,4,1,2,0]:
            return 12
        elif flat == [5,3,4,2,0,1]:
            return -1
        elif flat == [5,3,4,2,1,0]:
            return -1
        elif flat == [5,4,0,1,2,3]:
            return -1
        elif flat == [5,4,0,1,3,2]:
            return 9
        elif flat == [5,4,0,2,1,3]:
            return 13
        elif flat == [5,4,0,2,3,1]:
            return -1
        elif flat == [5,4,0,3,1,2]:
            return -1
        elif flat == [5,4,0,3,2,1]:
            return 13
        elif flat == [5,4,1,0,2,3]:
            return -1
        elif flat == [5,4,1,0,3,2]:
            return 10
        elif flat == [5,4,1,2,0,3]:
            return -1
        elif flat == [5,4,1,2,3,0]:
            return -1
        elif flat == [5,4,1,3,0,2]:
            return 11
        elif flat == [5,4,1,3,2,0]:
            return 12
        elif flat == [5,4,2,0,1,3]:
            return 8
        elif flat == [5,4,2,0,3,1]:
            return -1
        elif flat == [5,4,2,1,0,3]:
            return 7
        elif flat == [5,4,2,1,3,0]:
            return 8
        elif flat == [5,4,2,3,0,1]:
            return -1
        elif flat == [5,4,2,3,1,0]:
            return -1
        elif flat == [5,4,3,0,1,2]:
            return -1
        elif flat == [5,4,3,0,2,1]:
            return 12
        elif flat == [5,4,3,1,0,2]:
            return -1
        elif flat == [5,4,3,1,2,0]:
            return -1
        elif flat == [5,4,3,2,0,1]:
            return 13
        elif flat == [5,4,3,2,1,0]:
            return 14
        # Should never reach here because any permutation of 0..5 is covered
        return -1