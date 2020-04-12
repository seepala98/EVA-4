import numpy as np
import math
import matplotlib.pyplot as plt

def zigzag_plot(num_tri = 3, min_val = 0, max_val = 1, tri_base = 2):
    x = np.linspace(0, num_tri * tri_base, num=1000)
    tan_val = 2*(max_val-min_val)/tri_base
    print(tan_val)
    y = [i*tan_val for i in x]
    y = [abs(i - tri_base * np.floor((i+tri_base/2)/tri_base))* tan_val + min_val for i in x]
    plt.plot(x,y)
