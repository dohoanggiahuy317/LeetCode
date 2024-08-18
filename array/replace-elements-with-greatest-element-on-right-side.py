class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        
        l=[]
        curr_max = max(arr[1:])
        i = 1
        
        while i < len(arr):
            l.append(curr_max)
            if arr[i] == curr_max and i+1 < len(arr):
                curr_max = max(arr[i+1:])
            i+=1
            
        l.append(-1)
        return l