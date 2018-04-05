import sys
import numpy as np

size = int(sys.argv[1])

x = np.linspace(-5, 5, size)

y = np.sin(x * np.sin(x)**2)

data_folder = 'data/Q5'

np.savetxt(data_folder + '/data_x_5.txt', x)
np.savetxt(data_folder + '/data_y_5.txt', y)
