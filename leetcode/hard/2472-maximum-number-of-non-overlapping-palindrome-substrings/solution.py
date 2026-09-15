class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[i][j] = True if s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        for i in range(n):
            pal[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length == 2:
                        pal[i][j] = True
                    else:
                        pal[i][j] = pal[i + 1][j - 1]

        # dp[i] = maximum palindromes using first i characters
        dp = [0] * (n + 1)

        for i in range(n):
            # Skip s[i]
            dp[i + 1] = max(dp[i + 1], dp[i])

            # Select a palindrome starting at i
            for j in range(i + k - 1, n):
                if pal[i][j]:
                    dp[j + 1] = max(dp[j + 1], dp[i] + 1)

        return dp[n]