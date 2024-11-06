from typing import List
import heapq

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total_milestones = sum(milestones)
        max_milestone = max(milestones)
        
        # Calculate the sum of all other milestones besides the largest one
        sum_of_rest = total_milestones - max_milestone
        
        # If the largest project milestones are more than the rest, we can't alternate fully
        if max_milestone > sum_of_rest + 1:
            return 2 * sum_of_rest + 1
        else:
            # Otherwise, we can work all weeks
            return total_milestones