class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        indx_nums = list(zip([i for i in range(len(nums))], nums))
        snums = sorted(indx_nums, key=lambda x: x[1])


        num_gr = 0
        groups = {0: [snums[0]]}


        for i in range(1, len(snums)):
            if snums[i][1] - snums[i-1][1] > limit:
                num_gr += 1

            if num_gr not in groups:
                groups[num_gr] = []
            groups[num_gr].append( snums[i] )

        for _, v in groups.items():
            indx_li = list(map(lambda x: x[0], v))
            val_li = list(map(lambda x: x[1], v))

            val_li.sort()
            indx_li.sort()

            # print(indx_li, val_li)

            for i in range(len(indx_li)):
                nums[ indx_li[i] ] = val_li[i]

        return nums
  

                
        