class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        rate = []

        for i in range(len(dist)):
            rate.append(dist[i]/speed[i])

        rate.sort()

        time = 0
        while time < len(rate) and rate[time] > time:
            time += 1

        return time
        