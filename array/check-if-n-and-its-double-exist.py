class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        arr.sort()
        
        for i in range(len(arr)):
            if arr[i] * 2 in set(arr[i+1:]):
                return True

        return False