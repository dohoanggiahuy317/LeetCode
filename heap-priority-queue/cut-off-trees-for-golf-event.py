class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # CONSTANT
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        WALL, EMPTY = 0, 1
        m, n = len(forest), len(forest[0])
        CUT, UNCUT = True, False

        # GET ALL TREES IN ORDER
        tree_list = []
        for i, row in enumerate(forest):
            for j, tree in enumerate(row):
                if tree != WALL and forest[i][j] != EMPTY:
                    tree_list.append(forest[i][j])
        tree_list.sort()

        # BFS
        def bfs(s_x, s_y, target) -> (bool, int, int, int):
            queue = deque([(s_x, s_y)])
            reachable = set(queue)
            step = 0

            while queue:
                for _ in range(len(queue)):
                    c_x, c_y = queue.popleft()

                    if forest[c_x][c_y] == target:
                        return CUT, step, c_x, c_y
                    
                    for i, j in DIRECTIONS:
                        n_x, n_y = c_x + i, c_y + j

                        if not (0 <= n_x < m and 0 <= n_y < n):
                            continue

                        if forest[n_x][n_y] == WALL:
                            continue

                        if (n_x, n_y) in reachable:
                            continue

                        queue.append((n_x, n_y))
                        reachable.add((n_x, n_y))

                step += 1

            return UNCUT, -1, -1, -1

        
        # START CUTTING
        if not tree_list:
            return 0

        s_x, s_y = 0, 0
        ans = 0

        for tree in tree_list:
            cut, step, n_x, n_y = bfs(s_x, s_y, tree)

            if not cut:
                return - 1 

            s_x, s_y = n_x, n_y
            ans += step
            # print(s_x, s_y, tree, ans)
        
        return ans