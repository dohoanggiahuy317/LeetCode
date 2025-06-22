class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        s += fill * (0 if len(s) % k == 0 else k - len(s) % k)

        return [s[i:i+k] for i in range(0, len(s), k)]