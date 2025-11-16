class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        DIRS = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [3, 1, 5],
            5: [2, 4],
        }

        def pack_3bit(values):
            num_pack = 0
            x0 = -1

            for i, num in enumerate(values):
                num_pack = (num_pack << 3) | num
                if num == 0:
                    x0 = 5 - i

            return num_pack, x0

        def tile_swap(num_pack, x0):
            ALL_ONE = 7
            BIT_LENGTH = 3
            x0_shift = x0 * BIT_LENGTH

            neigh_packs = []
            for neigh_idx in DIRS[x0]:
                neigh_shift = neigh_idx * BIT_LENGTH
                bit_neigh = (num_pack >> neigh_shift) & ALL_ONE  

                neigh_pack = num_pack & ~(ALL_ONE << neigh_shift)
                neigh_pack = neigh_pack | (bit_neigh << x0_shift)

                neigh_packs.append((neigh_pack, neigh_idx))

            return neigh_packs
        
        TARGET, _ = pack_3bit([1,2,3,4,5,0])
        start = pack_3bit(board[0] + board[1])

        queue = deque([start])
        visited = set(queue)
        steps = 0

        while queue:
            for _ in range(len(queue)):
                num_pack, x0_idx = queue.popleft()

                if num_pack == TARGET:
                    return steps

                neigh_packs = tile_swap(num_pack, x0_idx)
                for neigh_pack, neigh_idx in neigh_packs:
                    if neigh_pack in visited:
                        continue
                
                    queue.append((neigh_pack, neigh_idx))
                    visited.add(neigh_pack)

            steps += 1
        
        return -1

        



        


