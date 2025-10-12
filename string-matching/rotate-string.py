class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        goal_li = deque(list(goal))
        s_li = list(s)
        for i in range(len(goal_li)):
            # print(goal_li, s_li)
            if list(goal_li) == s_li:
                return True
            goal_li.append(goal_li.popleft())


        return False