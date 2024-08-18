class Solution:
    def countSubstrings(self, s: str) -> int:
        distance = 0
        memoir = [[False] * len(s) for _ in range(len(s))]
        ans = 0

        while distance < len(s):
            # for x in memoir:
            #     print(x)
            # print(distance)
            # print()
            for i in range(len(s) - distance):
                if distance == 0:
                    memoir[i][i+distance] = True
                    ans += 1

                if distance == 1:
                    if s[i] == s[i+distance]:
                        memoir[i][i+distance] = True
                        ans += 1

                if distance > 1:
                    if s[i] == s[i+distance] and memoir[i+1][i + distance-1]:
                        memoir[i][i+distance] = True
                        ans += 1
                        
            distance += 1

        return ans