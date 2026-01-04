class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        # dp[i] = num of stable sub up to element i
        # 2 cases
        # nums[i] not involve -> dp[i - 1]
        # nums[i] does involve -> dp[i - 1]
        # dp[i] comprises of 4 things

        # if nums[i] = even
        
        #     odd_odd[i] = odd_odd[i - 1]
        #     even_even[i] = odd_even[i - 1] + 1
        #     odd_even[i] = odd_odd[i - 1] + even_odd[i - 1] + 1
        #     even_odd[i] = even_odd[i - 1]

        # if nums[i] = odd
        
        #     odd_odd[i] = even_odd[i - 1] + 1
        #     even_even[i] = even_even[i - 1]
        #     odd_even[i] = odd_even[i - 1]
        #     even_odd[i] = odd_even[i - 1] + even_even[i - 1] + 1

        # 2 3 4

        # odd_odd   0 0 0 0
        # even_even 0 0 1 5
        # odd_even  0 0 3 3
        # even_odd  0 2 2 2
        # odd       0 1 1 1
        # even      1 1 2 3

        n = len(nums)
        MOD = 10 ** 9 + 7
        
        odd       = [0] * n
        even      = [0] * n
        odd_odd   = [0] * n
        even_even = [0] * n
        odd_even  = [0] * n
        even_odd  = [0] * n

        if nums[0] % 2 == 1:
            odd[0] = 1
        else:
            even[0] = 1

        for i in range(1, n):
            num = nums[i]

            if num % 2 == 1: # odd
                
                even[i] = even[i - 1] % MOD
                even_even[i] = even_even[i - 1] % MOD
                odd_even[i] = odd_even[i - 1] % MOD

                # involve + not involve
                odd[i] = (odd[i - 1] + 1) % MOD

                # involve + not involve
                odd_odd[i] = (odd[i - 1] + even_odd[i - 1] + odd_odd[i - 1]) % MOD 

                # involve + not involve
                even_odd[i] = (even[i - 1] + even_even[i - 1] + odd_even[i - 1] + even_odd[i - 1]) % MOD 

            else: # even
                odd[i] = odd[i - 1] % MOD
                odd_odd[i] = odd_odd[i - 1] % MOD
                even_odd[i] = even_odd[i - 1] % MOD
                
                # involve + not involve
                even[i] = (even[i - 1] + 1) % MOD
                
                # involve + not involve
                even_even[i] = (even[i - 1] + odd_even[i - 1] + even_even[i - 1]) % MOD

                # involve + not involve
                odd_even[i] = (odd[i - 1] + odd_odd[i - 1] + even_odd[i - 1] + odd_even[i - 1]) % MOD
                
                

        # print(odd_odd)
        # print(even_even)
        # print(odd_even)
        # print(even_odd)
        # print(odd)
        # print(even)

        return (odd[-1] + even[-1] + odd_odd[-1] + even_even[-1] + odd_even[-1] + even_odd[-1]) % MOD

        

        