class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        n_pairs = sorted(pairs, key=lambda x: x[1])

        curr_tail = -1001
        ans = 0

        # print(n_pairs)

        for x in n_pairs:
            if x[0] > curr_tail:
                print(x)
                ans += 1
                curr_tail = x[1]

        return ans


        