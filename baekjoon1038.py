'''
https://www.acmicpc.net/problem/1038

백준 1038 감소하는 수 찾기.

DP? 부루트포스에 가까운 문제라고 생각한다.
1. 모든 감소수를 구하기 n< 1000000 보다 작다는 조건을 통해서.

'''

n = int(input())
dec_nums = []

def dec_num(num, nums, level = 1):
    if level > 10:
        return

    nums.append(num)

    for i in range(10):
        if num % 10 > i:
            dec_num((num * 10) + i , nums, level=level + 1)

    return nums

for num in range(10):
    r = dec_num(num, dec_nums)

r.sort()

if n >= 1023:
    print(-1)
else:
    print(r[n])
