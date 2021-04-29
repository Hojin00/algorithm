data = input()

result = int(data[0])


for i in range(1, len(data)):
    num = int(data[i])

    if num <= 1 or result <= 1:
        #if either result or num is 1 or 0, just add up.
        result += num
    else:
        result *= num

print(result)