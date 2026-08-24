t = int(input())

while t > 0:
    n, m = map(int, input().split())
    a = input()

    ones = a.count('1')
    total_ones = ones * m

    # If total number of 1s is odd,
    # it cannot be divided equally.
    if total_ones % 2 != 0:
        print(0)
        t -= 1
        continue

    target = total_ones // 2

    # Count how many positions in A have
    # each possible prefix number of 1s.
    freq = [0] * (ones + 1)

    prefix = 0

    for ch in a:
        if ch == '1':
            prefix += 1

        freq[prefix] += 1

    ans = 0

    # Check each copy of A.
    for copy in range(m):
        before = copy * ones
        required = target - before

        if 0 <= required <= ones:
            ans += freq[required]

    print(ans)

    t -= 1