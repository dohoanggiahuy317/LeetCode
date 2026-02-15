class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = sorted(nums[::2])              # ascending
        odd  = sorted(nums[1::2], reverse=True)  # descending

        i = j = 0
        out = []

        while i < len(even) and j < len(odd):
            out.append(even[i])
            out.append(odd[j])
            i += 1
            j += 1 

        # append leftovers
        out.extend(even[i:])
        out.extend(odd[j:])
        return out