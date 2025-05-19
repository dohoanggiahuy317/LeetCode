class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temp = []

        # for i in range(len(temperatures)):
        #     temp.append((i, temperatures[i]))
        ans = [0] * len(temperatures)
        # print(temp)

        for i in range(len(temperatures) - 1):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i
                    break

        return ans