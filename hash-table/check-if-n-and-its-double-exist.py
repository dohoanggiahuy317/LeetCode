class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s_arr = set(arr)

        if arr.count(0) == 2:
            return True

        for num in s_arr:
            if num * 2 in s_arr:
                return True
        
        return False