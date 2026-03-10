class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoes_map = defaultdict(int)
        ans = 0

        for l, r in dominoes:
            if l > r:
                l, r = r, l

            ans += dominoes_map[(l, r)]
            dominoes_map[(l, r)] += 1

        return ans