class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        LETTERS_MAPPING = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        n = len(digits)


        def add_number(num_added, curr_str):
            nonlocal ans, digits, n, LETTERS_MAPPING

            if num_added == n:
                ans.append(curr_str)
                return

            num = digits[num_added]
            for letter in LETTERS_MAPPING[num]:
                add_number(num_added + 1, curr_str + letter)
        
        if n == 0:
            return []

        ans = []
        add_number(0, "")
        return ans