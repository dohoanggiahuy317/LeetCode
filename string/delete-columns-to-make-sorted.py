class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0

        for index in range( len(strs[0]) ):
            for word in range(len(strs) - 1):
                if ord(strs[word][index]) > ord(strs[word+1][index]):
                    count += 1
                    break 

        return count