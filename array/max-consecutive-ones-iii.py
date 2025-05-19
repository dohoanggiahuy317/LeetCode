class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num0 = k
        ans = 0
        curr = 0
        trail = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                curr += 1
                ans = max(ans, curr)
                # print(trail, i, curr)
                continue
            
            else:
                if num0 > 0:
                    curr += 1
                    num0 -= 1
                    ans = max(ans, curr)
                    # print(trail, i, curr)
                    continue
                else:
                    while nums[trail] == 1:
                        trail += 1
                        curr -= 1
                    trail += 1         
                    num0 += 1
                    curr -= 1
                    
                    curr += 1
                    num0 -= 1
                    ans = max(ans, curr)
                    # print(trail, i, curr)

        return ans


