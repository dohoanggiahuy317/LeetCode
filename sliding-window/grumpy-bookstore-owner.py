class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        curr_stf = sum(c for c, g in zip(customers[:minutes], grumpy[:minutes]) if g == 1)
        max_stf = curr_stf

        for r in range(minutes, len(customers)):
            if grumpy[r] == 1:
                curr_stf += customers[r]
            if grumpy[r - minutes] == 1:
                curr_stf -= customers[r - minutes]

            max_stf = max(max_stf, curr_stf)

        alr_stf = sum(c for c, g in zip(customers, grumpy) if g == 0)
        return max_stf + alr_stf
