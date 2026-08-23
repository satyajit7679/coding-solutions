# cook your dish here
t = int(input())
while t > 0:
    n, m = map(int,input().split())
    a = input()
    total = a.count('1') * m
    ans = 0
    prefix = 0
    for i in range(m * n):
        curr = a[i % n]
        if curr =='1':
            prefix += 1
        sufix = total - prefix
        if prefix == sufix:
            ans += 1
    t -= 1
    print(ans)