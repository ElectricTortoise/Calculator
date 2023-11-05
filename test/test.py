import FPVCModule as fpvc
import numpy as np


a = np.array([1, 1, 0])
b = np.array([-1, 2, 4])
c = np.array([-2, 1, 3])

d = fpvc.get_vector_input(2, "direction")
print(d)
fpvc.normal_calc(d[0], d[1])