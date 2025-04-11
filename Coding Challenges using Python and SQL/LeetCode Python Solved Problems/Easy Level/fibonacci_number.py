# 309.) Fibonacci Number
# Categories: Math, Dynamic Progreamming, Recursion, Memoization

class Solution:
    def fib(self, n: int) -> int:
        def get_fibonacci_number(number: int) -> int:
            if number == 1:
                return 1
            
            elif number == 0:
                return 0
            
            result = get_fibonacci_number(number - 1) + get_fibonacci_number(number - 2)
            
            return result
        
        return get_fibonacci_number(n)
        