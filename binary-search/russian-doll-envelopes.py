class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        def finding_lis(li):
            
            ans = []
            ans.append(li[0])

            for i in range(1, len(li)):
                num = li[i]

                if ans[-1] < num:
                    ans.append(num)

                elif ans[-1] > num:
                    l, r = 0, len(ans) - 1
                    idx = len(ans)
                    while l <= r:
                        m = (l + r) // 2

                        if ans[m] > num:
                            idx = m
                            r = m - 1
                        else:
                            l = m + 1
                    ans[idx] = num
            
            return len(ans)

        envelopes.sort(key = lambda x: (x[0], -x[1]))
        curr_width = 0
        heights = []

        for w, h in envelopes:
            if w > curr_width:
                curr_width = w
                heights.append(h)

        return finding_lis(heights)


