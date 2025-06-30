class Solution:
    def findLHS(self, nums: List[int]) -> int:
        track = Counter(nums)
        ans = 0

        for num, count in track.items():
            if num - 1 in track:
                ans = max(ans, count + track[num-1])
            if num + 1 in track:
                ans = max(ans, count + track[num+1])
        
        return ans