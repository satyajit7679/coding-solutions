def solve(N, X, A):
    # write your code here
    for i in range(N):
        if A[i] == X:
            return "YES"
    return "NO"
        