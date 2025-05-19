from collections import defaultdict
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        d = defaultdict(list)
        for i in range(len(temperatures)):
            d[temperatures[i]].append(i)

        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            today = temperatures[i]
            temp = float("INF")
            for next_temp in range(today + 1, 101):
                while d[next_temp] and d[next_temp][0] < i:
                    d[next_temp].pop(0)
                if d[next_temp]:
                    temp = min(temp, d[next_temp][0] - i)
                    # print(d[next_temp])

            ans[i] = temp if temp != float("INF") else 0

            

        return ans