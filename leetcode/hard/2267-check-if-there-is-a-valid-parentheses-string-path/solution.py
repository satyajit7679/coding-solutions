
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        # Valid parentheses string must have even length
        if (m + n - 1) % 2 != 0:
            return False

        memo = {}

        def dfs(i, j, balance):
            # Invalid balance
            if balance < 0:
                return False

            # Not enough remaining cells to close parentheses
            remaining = (m - 1 - i) + (n - 1 - j)

            if balance > remaining:
                return False

            # Destination reached
            if i == m - 1 and j == n - 1:
                return balance == 0

            # Check memoization
            if (i, j, balance) in memo:
                return memo[(i, j, balance)]

            # Move right
            right = False
            if j + 1 < n:
                new_balance = balance + (1 if grid[i][j + 1] == '(' else -1)
                right = dfs(i, j + 1, new_balance)

            # Move down
            down = False
            if i + 1 < m:
                new_balance = balance + (1 if grid[i + 1][j] == '(' else -1)
                down = dfs(i + 1, j, new_balance)

            memo[(i, j, balance)] = right or down

            return memo[(i, j, balance)]

        # Start from top-left cell
        initial = 1 if grid[0][0] == '(' else -1

        return dfs(0, 0, initial)