class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)

        # i + zeros means “how many zeros remain to the left” 
        # or “how many shifts still apply” for positions at/left of i

        for i in range(len(arr) - 1, -1, -1):
            if i + zeros < len(arr):
                arr[i + zeros] = arr[i]
            
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < len(arr):
                    arr[i + zeros] = 0