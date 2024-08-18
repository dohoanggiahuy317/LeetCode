class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def bfs(source):
            nonlocal d, visited, que

            curr = source

            while len(que) > 0:
                curr = que.pop(0)

                num11 = str((int(curr[0]) + 1) % 10) + curr[1:]
                num12 = str((int(curr[0]) - 1) % 10) + curr[1:]
                num21 = curr[0] + str((int(curr[1]) + 1) % 10) + curr[2:]
                num22 = curr[0] + str((int(curr[1]) - 1) % 10) + curr[2:]
                num31 = curr[:2] + str((int(curr[2]) + 1) % 10) + curr[3:]
                num32 = curr[:2] + str((int(curr[2]) - 1) % 10) + curr[3:]
                num41 = curr[:3] + str((int(curr[3]) + 1) % 10)
                num42 = curr[:3] + str((int(curr[3]) - 1) % 10)
                li = [num11, num12, num21, num22, num31, num32, num41, num42]

                for adj in li:
                    if visited[adj] == False:
                        que.append(adj)
                        d[adj] = d[curr] + 1
                        visited[adj] = True

                if curr == target:
                    print("stop")
                    return
                
        d = {}
        visited = {}
        que = ["0000"]
        for i in range(0, 10000):
            si = "0" * (4 - len(str(i))) + str(i)
            visited[si] = False
            d[si] = -1

        visited["0000"] = True
        d["0000"] = 0

        for x in deadends:
            visited[x] = True

        if "0000" in deadends:
            return -1


        bfs("0000")
        return d[target]