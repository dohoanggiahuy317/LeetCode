class Solution:
    def trap(self, height: List[int]) -> int:

        start, end = 0, len(height) - 1

        while start < len(height) - 1 and height[start] < height[start + 1]:
            start += 1
        while end > 0 and height[end] < height[end - 1]:
            end -= 1

        if end <= start:
            return 0

        track = []

        for i in range(start, end + 1):
            track.append((i, height[i]))

        track.sort(key = lambda x: x[1], reverse = True)

        ans = 0
        min_range = min(track[0][0], track[1][0])
        max_range = max(track[0][0], track[1][0])

        lower_bank = min(height[min_range], height[max_range])
        for col_ind in range(min_range, max_range + 1):
            ans += max(0, lower_bank - height[col_ind])

        track.pop(0)
        track.pop(0)

        while track:
            next_col = track.pop(0)[0]
            if min_range < next_col < max_range:
                continue
            
            elif next_col > max_range:
                for col_ind in range(max_range, next_col + 1):
                    ans += max(0, height[next_col] - height[col_ind])
                
                max_range = next_col

            elif next_col < max_range:
                for col_ind in range(next_col, min_range + 1):
                    ans += max(0, height[next_col] - height[col_ind])
                
                min_range = next_col

        return ans
           
        
