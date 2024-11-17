class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pref_sum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            pref_sum[i+1] = pref_sum[i] + nums[i]

        # print(pref_sum)

        index_queue = []
        ans = float("INF")

        for i in range(len(nums) + 1):
            while index_queue and pref_sum[i] - pref_sum[index_queue[0]] >= k:
                ans = min(ans, i - index_queue.pop(0))

            while index_queue and pref_sum[index_queue[-1]] >= pref_sum[i]:
                index_queue.pop(-1)

            index_queue.append(i)

        return -1 if ans == float("INF") else ans

                    


            