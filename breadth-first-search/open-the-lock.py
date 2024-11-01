class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def bfs():
            nonlocal q, target, visited, ans

            while q:
                curr, t = q.pop(0)

                num11 = str((int(curr[0]) + 1) % 10) + curr[1:]
                num12 = str((int(curr[0]) + 9) % 10) + curr[1:]
                num21 = curr[:1] + str((int(curr[1]) + 1) % 10) + curr[2:]
                num22 = curr[:1] + str((int(curr[1]) + 9) % 10) + curr[2:]
                num31 = curr[:2] + str((int(curr[2]) + 1) % 10) + curr[3:]
                num32 = curr[:2] + str((int(curr[2]) + 9) % 10) + curr[3:]
                num41 = curr[:3] + str((int(curr[3]) + 1) % 10)
                num42 = curr[:3] + str((int(curr[3]) + 9) % 10)
                li = [num11, num12, num21, num22, num31, num32, num41, num42]

                for neigh in li:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.append((neigh, t + 1))


                if curr == target:
                    ans = t
                    return t


        visited = set()
        for n in deadends:
            visited.add(n)
        if "0000" in visited:
            return -1
        visited.add("0000")

        q = [("0000", 0)]
        ans = -1
        bfs()

        return ans

