class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(int)
        max_len = 0

        for i in range(1, n + 1):
            digits = str(i)
            sum_digits = sum(map(int, digits))

            groups[sum_digits] += 1
            max_len = max(max_len, groups[sum_digits])

        ans = 0
        for group_len in groups.values():
            ans += 1 if group_len == max_len else 0

        return ans
            