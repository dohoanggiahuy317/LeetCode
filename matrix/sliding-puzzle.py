SWAP_DIRECTIONS = {
                0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 
                3: [0, 4], 4: [1, 3, 5], 5: [2, 4], 
            }

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # CONSTANT
        m, n = len(board), len(board[0])
        length = m * n
        MASK = (1 << 3) - 1

        def pack_3bit(values):
            pack_num = 0
            x0 = -1
            for i, v in enumerate(values):
                pack_num = (pack_num << 3) | v
                if v == 0:
                    x0 = i
            return pack_num, x0

        def tile_swap(board_1d, x0):
            nonlocal length
            
            neighs = []
            x0_shift = (length - 1 - x0) * 3

            for di in SWAP_DIRECTIONS[x0]:
                
                di_shift = (length - 1 - di) * 3
                di_pack = (board_1d >> di_shift) & MASK

                # Clear the 3-bit at the postion that will be swapped with 0
                neigh = board_1d & ~(MASK << di_shift)

                # Set the 3-bit at postion that used to 0 to current pack 
                neigh = neigh | (di_pack << x0_shift)
                
                neighs.append((neigh, di))

            return neighs

        TARGET, _ = pack_3bit([1, 2, 3, 4, 5, 0])
        board_1d, x0 = pack_3bit(cell for row in board for cell in row)

        # BFS
        queue = deque( [(board_1d, x0)] )
        reachable = set()
        step = 0

        while queue:
            for _ in range(len(queue)):
                curr_board_1d, curr_x0 = queue.popleft()

                if curr_board_1d == TARGET:
                    return step

                for neigh, new_x0 in tile_swap(curr_board_1d, curr_x0):
                    if (neigh, new_x0) in reachable:
                        continue
                    
                    queue.append((neigh, new_x0))
                    reachable.add((neigh, new_x0))

            step += 1

        return -1

        

