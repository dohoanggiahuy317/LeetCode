SWAP_DIRECTIONS = {
                0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 
                3: [0, 4], 4: [1, 3, 5], 5: [2, 4], 
            }

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])

        TARGET = "123450"
        board_1d = "".join( [str(val) for row in board for val in row] )
        x0 = board_1d.index("0")

        def get_next_states(board_1d, x0):
            nonlocal m, n
            neighs = []

            for direction in SWAP_DIRECTIONS[x0]:
                board_li = list(board_1d)
                board_li[x0], board_li[direction] = board_li[direction], board_li[x0]
                neighs.append(("".join(board_li), direction))

            return neighs

        # BFS
        queue = deque( [(board_1d, x0)] )
        reachable = set()
        step = 0

        while queue:
            for _ in range(len(queue)):
                curr_board_1d, curr_x0 = queue.popleft()

                if curr_board_1d == TARGET:
                    return step

                for neigh, new_x0 in get_next_states(curr_board_1d, curr_x0):
                    if (neigh, new_x0) in reachable:
                        continue
                    
                    queue.append((neigh, new_x0))
                    reachable.add((neigh, new_x0))

            step += 1

        return -1

        

