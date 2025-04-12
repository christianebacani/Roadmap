# 2283.) Check if Number Has Equal Digit Count and Digit Value
# Categories: Hash Table, String, Counting

class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            if num.count(str(i)) != int(num[i]):
                return False
        
        return True
