if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    max = -101
    mid = -101
    for i in range(n):
        if arr[i] > max:
            mid = max
            max = arr[i]
        elif arr[i] > mid and arr[i] < max:
            mid = arr[i]
    print(mid)