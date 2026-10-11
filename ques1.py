N, K = map(int, input().split())
arr = list(map(int, input().split()))

current_sum = sum(arr[:K])
max_sum = current_sum

for i in range(K, N):
    current_sum += arr[i] - arr[i - K]
    if current_sum > max_sum:
        max_sum = current_sum

print("maximum sum:", max_sum)