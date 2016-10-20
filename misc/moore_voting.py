array = map(int, raw_input().strip().split())
maj_i = 0
count = 1
for i in range(1, len(array)):
    if array[maj_i] == array[i]:
        count += 1
    else:
        count -= 1

    if count == 0:
        maj_i = i
        count = 1

    print maj_i

print array[maj_i]
