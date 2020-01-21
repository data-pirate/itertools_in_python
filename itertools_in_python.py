from itertools import count

# count method in itertools

for i in count(10):
    if i > 20:
        break
    else:
        print(i)
