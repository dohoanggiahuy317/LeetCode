class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        parent = {}
        size = {}
        max_size = 1

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            nonlocal max_size
            i_p = find(i)
            j_p = find(j)

            if i_p != j_p:
                parent[i_p] = j_p
                size[j_p] += size[i_p]
                max_size = max(max_size, size[j_p])

        for num in nums:
            if num not in parent:
                parent[num] = num
                size[num] = 1
            if num - 1 in parent:
                union(num, num - 1)
            if num + 1 in parent:
                union(num, num + 1)
        
        return max_size

                