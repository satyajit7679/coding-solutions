# cook your dish here
T = int(input())

while T > 0:
    N = int(input())
    arr = list(map(int,input().split()))
    max_ele = arr[0]
    for i in range(1,N):
        if arr[i] > max_ele:
            max_ele = arr[i]
    print(max_ele)
    T -= 1