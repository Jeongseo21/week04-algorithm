import sys
input = sys.stdin.readline

nums = [0]*(30001)


N = int(input())
for i in range(2, N+1):
    nums[i] = nums[i-1]+1
    if i % 2 == 0:
        nums[i] = min(nums[i], nums[i//2] + 1)
    if i % 3 == 0:
        nums[i] = min(nums[i], nums[i//3] + 1)
    if i % 5 == 0:
        nums[i] = min(nums[i], nums[i//5] + 1)

print(nums[N])