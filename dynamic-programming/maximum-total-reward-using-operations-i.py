class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()  
        ans = {0}  
        
        for reward in rewardValues:
            local_score = set()
            
            for prev_score in ans:
                if reward > prev_score:
                    local_score.add(reward + prev_score)
            
            ans.update(local_score)
        
        # print(ans)
        
        return max(ans)