class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        start = 0
        end = 1
        div = 0
        ans = []

        while end < len(s)+1:
            if end == len(s):
                ans.append(s[div:end])
                end += 1

            if s[start] in s[end:]:
                end += 1
            else:
                start += 1
                if start == end:
                    ans.append(s[div : start])
                    div = start
                    end += 1
                    
        return list(map(lambda x: len(x), ans))
