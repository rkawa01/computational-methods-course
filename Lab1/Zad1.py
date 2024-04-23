import numpy as np
import timeit
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

count = 10**7
# rand = 0.7132670253265855
# rand = 0.9384460290750193
rand = 0.53125
# rand = np.random.random(1)[0]
v32 = np.float32(rand)
v64 = np.float64(rand)
expected = rand*count

def sum(get_plot=False):
    d = []
    # print(great_val)
    sum_32 = np.float32(0)
    sum_64 = np.float64(0)
    for i in range(count):
        if (i%25000 == 0 and get_plot):
            abs_val = abs(sum_32 - sum_64)
            percentage = abs_val / expected * 100
            d.append(percentage)
        sum_32 += v32
        sum_64 += v64

    if(get_plot):
        sns.lineplot(data=d)
        plt.show()

    #Wypisanie błędu dla float32
    abs_val = abs(sum_32 - expected)
    percentage = abs_val/expected * 100
    print("Błąd bezwzględny: " + str(abs_val))
    print("Błąd względny: " + str(percentage))

def recursive():
    def recursive_sum(v,c,pos=0):
        if c == 1:
            return v
        else:
            return recursive_sum(v,c//2,pos) + recursive_sum(v,c-c//2,pos+c//2)

    sum_32 = recursive_sum(v32,count)
    abs_val = abs(sum_32 - expected)
    percentage = abs_val / expected * 100
    print("Błąd bezwzględny: " + str(abs_val))
    print("Błąd względny: " + str(percentage))
print(f"Czas: {timeit.timeit(lambda: sum(True),number=1)}s")
print(f"Czas: {timeit.timeit(lambda: recursive(),number=1)}s")


''' Dwukrotnie wolniej działa algorytm rekurencyjny '''