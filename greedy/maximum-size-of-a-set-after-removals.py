class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        d1 = {}
        d2 = {}
        n = len(nums1)
        posi = list(set(nums1 + nums2))

        for x in nums1:
            if x not in d1:
                d1[x] = 1
            else:
                d1[x] += 1
        for x in nums2:
            if x not in d2:
                d2[x] = 1
            else:
                d2[x] += 1


        curr1 = 0
        curr2 = 0

        for x in posi:
            if x in d1:
                curr1 += d1[x] - 1
                d1[x]  = 1
            if x in d2:
                curr2 += d2[x] - 1
                d2[x]  = 1

        s = 0
        while curr1 < n/2 and s < len(posi):
            curr_char = posi[s]
            if curr_char in d1 and d1[curr_char] != 0:
                if curr_char in d2 and d2[curr_char] != 0:
                    curr1 += 1
                    d2[curr_char] = 0
            s += 1

        s = 0
        while curr2 < n/2 and s < len(posi):
            curr_char = posi[s]
            if curr_char in d2 and d2[curr_char] != 0:
                if curr_char in d1 and d1[curr_char] != 0:
                    curr2 += 1
                    d1[curr_char] = 0
            s += 1


        s = 0
        while curr1 < n/2 and s < len(posi):
            curr_char = posi[s]
            if curr_char in d1 and d1[curr_char] != 0:
                curr1 += 1
                d1[curr_char] = 0
            s += 1

        s = 0
        while curr2 < n/2 and s < len(posi):
            curr_char = posi[s]
            if curr_char in d2 and d2[curr_char] != 0:
                curr2 += 1
                d2[curr_char] = 0
            s += 1


        ans = set()

        for x, y in d1.items():
            if y != 0:
                ans.add(x)
        for x, y in d2.items():
            if y != 0:
                ans.add(x)

        return len(ans)
        print(ans)
        
            