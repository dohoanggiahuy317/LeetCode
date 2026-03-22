class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people) - 1
        count = 0
        people.sort()

        while l <= r:
            count += 1

            if people[l] + people[r] > limit:
                r -= 1
            else:
                l += 1
                r -= 1

        return count
