class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def check_valid(query, pattern):
            pointer = 0

            for letter in query:
                if pointer == len(pattern) or letter != pattern[pointer]:
                    if letter.isupper():
                        return False
                    continue

                pointer += 1
                
            return pointer == len(pattern)


        return [check_valid(query, pattern) for query in queries]