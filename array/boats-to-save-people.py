class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l, r = 0, len(people) - 1

        ans = 0

        while l < r:
            if people[l] + people[r] > limit:
                r -= 1
            else:
                r -= 1
                l += 1
            
            ans += 1

        if l == r and people[l] <= limit:
            ans += 1

        return ans