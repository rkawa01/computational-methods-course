import numpy as np
import timeit

count = 10**7
# print("?")
rand = 0.713267025326585524
# rand = np.random.random(1)[0]
# rand = 0.666664
v32 = np.float32(rand)
v64 = np.float64(rand)
expected = rand*count

def Khan():

    sum_32 = np.float32(0)
    err = np.float32(0)
    for i in range(count):
        y = v32 - err
        temp = sum_32 + y
        err = (temp-sum_32)-y
        sum_32 = temp

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
print(f"Czas: {timeit.timeit(lambda: Khan(),number=1)}s")
print(f"Czas: {timeit.timeit(lambda: recursive(),number=1)}s")

