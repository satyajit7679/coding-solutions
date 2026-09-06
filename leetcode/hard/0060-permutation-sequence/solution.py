class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]

        factorial = 1
        for i in range(1, n):
            factorial *= i

        k -= 1

        result = []

        for i in range(n - 1, -1, -1):

            index = k // factorial

            result.append(numbers[index])

            numbers.pop(index)

            if i > 0:
                k = k % factorial
                factorial = factorial // i

        return ''.join(result)