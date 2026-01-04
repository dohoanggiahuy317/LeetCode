class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        n = len(nums1)
        cnt, intv = 0, 0

        for i in range(1, n):
            if nums1[i] > nums1[i-1] and nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                ans += min(cnt, intv + 1 - cnt)
                # print("c1", i, cnt, intv, ans)
                # print()
                intv = 0
                cnt = 0
            else:
                intv += 1
                if nums1[i] <= nums1[i-1] or nums2[i] <= nums2[i-1]:
                    cnt += 1
                    nums1[i], nums2[i] = nums2[i], nums1[i]
                # print("c2", i, cnt, intv, ans)
        
        ans += min(cnt, intv + 1 - cnt)

        return ans