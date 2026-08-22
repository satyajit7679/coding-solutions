class Solution:
    def cal_sum_squre(self, n):
        curr_sum = 0
        while n > 0:
            r = n % 10
            n = n // 10
            curr_sum += r * r
        return curr_sum
    def isHappy(self, n: int) -> bool:
        
        slow = n
        fast = n
        while True:
            slow = self.cal_sum_squre(slow)
            fast = self.cal_sum_squre(fast)
            fast = self.cal_sum_squre(fast)
            if fast == 1:
                return True
            if slow == fast:
                return False

        