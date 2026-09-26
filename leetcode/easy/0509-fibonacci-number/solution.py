class Solution:
    def fib(self, n: int) -> int:
        def fun(n):
            if n == 0 or n == 1:
                return n
            
            return fun(n - 1) + fun(n - 2)

        return fun(n)