class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        left = 0
        freq = defaultdict(int)
        ans = 0

        for right, fruit in enumerate(fruits):
            freq[fruit] += 1

            while len(freq) > 2:
                freq[fruits[left]] -= 1
                
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]

                left += 1

            ans = max(ans, right - left + 1)
            # print(left, right, freq)

        return ans


            

            