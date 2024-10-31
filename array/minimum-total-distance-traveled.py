class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        dp = [[0 for w in range(len(robot))] for _ in range(len(factory))]
        fact_stat = [[0 for w in range(len(robot))] for _ in range(len(factory))]

        for i in range(len(factory)):
            for j in range(len(robot)):
                curr_dist = abs(robot[j] - factory[i][0])
                fact_id = factory[i][0]

                if i == 0:
                    if j == 0:
                        dp[i][j] = curr_dist
                        fact_stat[0][0] = 1
                    else:
                        if fact_stat[i][j-1] < factory[0][1]:
                            dp[i][j] = dp[i][j-1] + curr_dist
                            fact_stat[0][j] = fact_stat[0][j-1] + 1
                        else:
                            dp[0][j] = float("INF")
                
                else:
                    if j == 0:
                        dp[i][j] = dp[i-1][j]
                        fact_stat[0][0] = 1
                    else:
                        if fact_stat[i][j-1] < factory[0][1]:
                            if dp[i-1][j] > dp[i][j-1] + curr_dist:
                                dp[i][j] = dp[i][j-1] + curr_dist
                                fact_stat[i][j] = fact_stat[i][j-1] + 1
                            else:
                                dp[i][j] = dp[i-1][j]
                        else:
                            dp[0][j] = float("INF")
    
        return dp[-1][-1]
