class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        indices_map = {}
        
        # loop qua nums và lưu cái index của số val gần nhát
        for j, num in enumerate(nums):

            # nếu mình có gặp lại số val, thì check khoảng cái j (index mới) - i (index gần nhất)
            # nếu mà khoảng cách <= k: return True
            if num in indices_map and j - indices_map[num] <= k:
                return True
            
            indices_map[num] = j

        return False