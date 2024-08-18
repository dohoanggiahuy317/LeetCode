class Solution:
    sub_li = []
    
    def gen_sub(self, candidates, target, sub, k):
        s = sum(sub)
        if s > target:
            if sum(sub[:-1]) == target and sub[:-1] not in self.sub_li:
                self.sub_li.append(sub[:-1])
            return
        if k == len(candidates):
            return

        self.gen_sub(candidates, target, sub, k+1)

        sub.append(candidates[k])
        self.gen_sub(candidates, target, sub, k)

        sub.pop()


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.sub_li = []
        self.gen_sub(candidates, target, [], 0)
        return self.sub_li
        