class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for x in nums:
            if x in dic.keys():
                dic[x] += 1
            else:
                dic[x] = 1

        
        dic_sorted = list(sorted(dic.items(), key=lambda x: x[1], reverse=True))

        # print(dic_sorted)
        return list(map(lambda x: x[0], dic_sorted[:k]))