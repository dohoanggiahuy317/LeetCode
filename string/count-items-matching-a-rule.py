class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        RULE_KEY_MAP = {
            "type": 0, 
            "color": 1,
            "value": 2
        }

        rule_value_idx = RULE_KEY_MAP[ruleKey]
        ans = 0

        for item in items:
            if item[rule_value_idx] == ruleValue:
                ans += 1

        return ans