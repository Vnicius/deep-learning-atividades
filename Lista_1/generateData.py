import sys
import random

classes = ["1,-1,-1,-1,-1,-1,-1,-1", "-1,1,-1,-1,-1,-1,-1,-1", "-1,-1,1,-1,-1,-1,-1,-1", "-1,-1,-1,1,-1,-1,-1,-1",
           "-1,-1,-1,-1,1,-1,-1,-1", "-1,-1,-1,-1,-1,1,-1,-1", "-1,-1,-1,-1,-1,-1,1,-1", "-1,-1,-1,-1,-1,-1,-1,1"]


bases = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [
    0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 1]]

num_samples = int(sys.argv[1])
data = []

for i, base in enumerate(bases):
    for _ in range(num_samples):
        number = base[:]
        for j, num in enumerate(number):
            if random.random() > 0.5:
                if random.random() > 0.5:
                    number[j] += 0.1
                else:
                    number[j] = -0.9 if not num else num - 1

        data.append([number, i])

random.shuffle(data)

out_x = open('./data_x.txt', 'w')
out_y = open('./data_y.txt', 'w')

for d in data:
    out_x.write(','.join([str(num) for num in d[0]]) + "\n")
    out_y.write(classes[d[1]] + "\n")
