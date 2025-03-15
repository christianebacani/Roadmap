# 1773.) Count Items Matching a Rule
# Categories: Array, String

class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        rules = {
            'type': 0,
            'color': 1,
            'name': 2
        }
        count = 0

        for item in items:
            if ruleValue == item[rules[ruleKey]]:
                count += 1
    
        return count
