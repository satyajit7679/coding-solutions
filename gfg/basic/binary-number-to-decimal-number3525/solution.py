class Solution:
	def binaryToDecimal(self, b):
		# code here
		b = int(b)
        p = 0
        ans = 0
        while b != 0:
            r = b % 10
            ans = ans + ((2**p)*r)
            p += 1
            b = b // 10

        return ans