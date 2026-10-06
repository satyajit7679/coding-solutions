class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        def fun(open, close, n, temp, res):

            if open == n and close == n:
                res.append(temp)
                return

            if open < n:
                temp = temp + '('
                fun(open + 1, close, n, temp, res)
                temp = temp[:-1]

            if close < open:
                temp = temp + ')'
                fun(open, close + 1, n, temp, res)
                temp = temp[:-1]

        res = []
        fun(0, 0, n, "", res)

        return res