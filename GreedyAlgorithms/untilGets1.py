# 1이 될 때까지 
# 1. n을 계속 1로 뺀다.
# 2. 이때 만약에 k로 나눌 수 있는 숫자가 나오면 k로 나눈다.
# 3. 더이상 k로 나누지 못하게 될 때 다시 1로 뺀다
# 4. 반복 1이 될 때까지

n, k = map(int, input().split())
# n = number that we want to get to 1
# k = number that we want to divide

results = 0

while True:
    target = (n // k) * k 
    # n 숫자가 있다고 치고 k로 나눌 수 있는 n에서 제일 가까운 숫자를 찾기 위함.
    # Ex. n=50 k=3 then, target = 48.

    results += (n - target)
    # subtract until the number divisible

    n = target
    # n is always current number

    if n < k:
        break
    # if n is smaller than k, it means that we just need to subtract by 1 until gets 1
    # no more dividing process

    # if it's not
    n //= k
    # divide by k

    results += 1
    # and add up in count

results += (n - 1)
# add up rest of number in count

print(results)
