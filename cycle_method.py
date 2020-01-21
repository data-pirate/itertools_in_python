from itertools import cycle
count = 0
for item in cycle('DAMAN'):
    if count > 9:
        break
    print(item)
    count += 1

# D
# A
# M
# A
# N
# D
# A
# M
# A
# N
