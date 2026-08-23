# cook your dish here

t = int(input())

while t > 0:
    n, m = map(int, input().split())
    a = input()

    total_ones = a.count('1') * m

    prefix_ones = 0
    ans = 0

    for i in range(n * m):
        if a[i % n] == '1':
            prefix_ones += 1

        suffix_ones = total_ones - prefix_ones

        if prefix_ones == suffix_ones:
            ans += 1

    print(ans)

    t -= 1