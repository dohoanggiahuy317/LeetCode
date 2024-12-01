class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        for i in range(len(arr)):
            if arr[i] % 2 == 0 and arr[i] // 2 in set(arr):
                return True

        return False