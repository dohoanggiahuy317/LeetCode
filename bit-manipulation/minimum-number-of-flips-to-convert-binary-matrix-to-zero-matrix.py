class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        # CONSTANT
        m, n = len(mat), len(mat[0])
        length = m * n
        TARGET = 0

        # HELPER
        def flatten(mat):
            nonlocal m, n
            val = 0
            for i in range(m):
                for j in range(n):
                    val = val * 2 + mat[i][j]
        
            return val

        def find_neigh(val):
            nonlocal length
            neigh_list = []

            for i in range(length - 1, -1, -1):
                temp = val

                # flip that i-th bit
                temp ^= (1 << i)
    
                # flip 2 horizontal neighbor
                if i % n != 0:
                    temp ^= (1 << (i - 1))
                if i % n != (n-1):
                    temp ^= (1 << (i + 1))

                # flip 2 vertica neighbor
                if i >= n:
                    temp ^= (1 << (i - n))
                if i < length - n:
                    temp ^= (1 << (i + n))

                neigh_list.append(temp)

            return neigh_list

        # BFS
        start_val = flatten(mat)
        queue = deque([start_val])
        reachable = set(queue)
        step = 0

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()

                if curr == TARGET:
                    return step

                for neigh in find_neigh(curr):
                    if neigh in reachable:
                        continue
                    queue.append(neigh)
                    reachable.add(neigh)
            step += 1

        return -1

        