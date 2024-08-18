class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        temp = colors + [colors[0]] + [colors[1]]
        ans = 0
        for i in range(1, len(temp) - 1):
            if temp[i] != temp[i-1] and temp[i-1] == temp[i+1]:
                ans += 1
        # 0 1 0 0 1 0 1 0 0 1
        return ans