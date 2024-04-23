import numpy as np
x0 = 0.5
x_n = np.float32(x0)
r = 2
for i in range(10**3):

    x_n = 1*x_n*(1-x_n)
    print(f"x{i+1} = {x_n}")