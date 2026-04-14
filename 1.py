def sum_neg(arr):
    n = len(arr)
    if n < 2:
        return 0

    max_val = arr[0]
    min_val = arr[0]
    max_i = 0
    min_i = 0

    for i in range(1, n):
        if arr[i] > max_val:
            max_val = arr[i]
            max_i = i
        if arr[i] < min_val:
            min_val = arr[i]
            min_i = i

    l = min(max_i, min_i)
    r = max(max_i, min_i)

    s = 0
    for i in range(l + 1, r):
        if arr[i] < 0:
            s += arr[i]
    return s


n = int(input("N: "))
arr = list(map(int, input().split()))
print("Result:", sum_neg(arr))
