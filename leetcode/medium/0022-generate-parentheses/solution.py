
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(curr, open_count, close_count):
            # Base case: n pairs are completed
            if len(curr) == 2 * n:
                result.append(curr)
                return

            # Add opening bracket if available
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)

            # Add closing bracket only when valid
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)

        return result
