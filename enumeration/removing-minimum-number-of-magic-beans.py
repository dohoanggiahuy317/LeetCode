class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        n = len(beans) + 1
        total = sum(beans)

        beans.sort()
        beans = [0] + beans

        ans = total
        # print(beans)

        for i, bean in enumerate(beans):
            total_target = (n - i) * bean
            remove_needed = total - total_target
            ans = min(ans, remove_needed)
            # print(i, bean, total_target, remove_needed)

        return ans
