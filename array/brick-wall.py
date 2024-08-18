class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d = Counter()

        for i in range(len(wall)):
            row = wall[i]
            cur_sum = 0

            for j in range(len(row) - 1):
                cur_sum += row[j]
                d[cur_sum] += 1
        if len(d.values()) == 0:
            return len(wall)
        return len(wall) - max(list(d.values()))