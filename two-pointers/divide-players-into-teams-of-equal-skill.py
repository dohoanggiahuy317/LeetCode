class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        num_team = n // 2
        s = sum(skill)

        if s % num_team != 0:
            return -1

        target_s = s // num_team
        ans = 0
        counter = Counter(skill)

        for u, v in counter.items():
            target_u = target_s - u
            if counter[target_u] != v:
                return -1
            ans += v * u * target_u

        return ans // 2
        
