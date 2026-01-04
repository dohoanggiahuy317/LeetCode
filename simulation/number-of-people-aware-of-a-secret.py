class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        # f(i) = number of new ppl know the info on day i
        # f(i) = f(i-delay) + f(i-delay-1) + ... +  f(i-forget)
        # f(1) = 1
        # f(i < 1) = 0

        # total_in_forget_days = f(n) + f(n-1) + ... + f(n - forget)
        # total_in_delay_days = f(n-delay) + f(n-delay-1) + ... + f(n-forget)

        # forget = 4, delay = 2
        # day_span = [0, 0, 0, 1], total_in_forget_days = 1 -> NEED total_in_delay_days = 0
        # 
        # [0, 0, 1, 0], total_in_forget_days = 1 -> NEED total_in_delay_days = 1
        # [0, 1, 0, 1], total_in_forget_days = 2 -> NEED total_in_delay_days = 1
        # [1, 0, 1, 1], total_in_forget_days = 3 -> NEED total_in_delay_days = 1
        # [1, 1, 1, 1], total_in_forget_days = 4 -> NEED total_in_delay_days = 2
        # [1, 1, 1, 2], total_in_forget_days = 5 -> NEED total_in_delay_days = X

        # last_day = day_span remove the lastest elemt
        # update the total_in_delay_days += day_span[forget - delay] - last_day
        # add the total_in_delay_days in to day_span
        # update the total_in_forget_days with total_in_delay_days and last_day


        MOD = 10 ** 9 + 7

        day_span = deque([int(i == forget - 1) for i in range(forget)])
        total_in_forget_days = 1
        total_in_delay_days = 0
        start_telling = forget - delay - 1

        for _ in range(n - 1):
            # step 1
            last_day = day_span.popleft()
            
            # step 2
            total_in_delay_days += day_span[start_telling] - last_day
            new_day = total_in_delay_days

            # step 3
            day_span.append(new_day)

            # step 4
            total_in_forget_days = ((total_in_forget_days + new_day) % MOD - last_day) % MOD

            # print(day_span, total_in_forget_days, total_in_delay_days)

        return total_in_forget_days


