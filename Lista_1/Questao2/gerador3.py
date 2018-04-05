import sys
import random
import numpy as np

size = int(sys.argv[1])
tipo = sys.argv[2]

out_file_x = open('data_x-3'+tipo+'.txt', 'w')
out_file_y = open('data_y-3'+tipo+'.txt', 'w')

out_data = []

if tipo == 'a':
    dict_x = ["0,0", "0,1", "1,0", "1,1"]
    dict_y = [0, 1, 1, 0]

    for _ in range(size):
        rd = random.randint(0, 3)

        out_data.append([dict_x[rd], dict_y[rd]])

elif tipo == 'b':
    for _ in range(size):
        x = random.random() * 4
        y = np.sin(np.pi * x) / (np.pi * x)

        out_data.append([x, y])

random.shuffle(out_data)

for data in out_data:
    out_file_x.write(str(data[0])+'\n')
    out_file_y.write(str(data[1])+'\n')
