t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    s = float('-inf')
    max_ele = a[0]
    for i in range(1,n):
        if a[i] > max_ele:
            s = max_ele
            max_ele = a[i]
        elif max_ele != a[i] > s:
            s = a[i]
    print(s + max_ele)
    
