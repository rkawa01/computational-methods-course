import numpy as np
import timeit

s = [2,3.6667,5,7.2,10]
n = [50,100,200,500,1000]
def formula_sum(k,s,v=True):
    if v:
        return np.float32(1/ k ** s)
    return np.float64(1/ k ** s)
def formula_dirichlet(k,s,v=True):
    if v:
        return np.float32((-1) ** (k-1) * 1/ k ** s)
    return np.float64((-1) ** (k-1) * 1/ k ** s)
def sums(form=True):

    for i in range(len(s)):
        sum_32_normal = np.float32(0)
        sum_32_descending = np.float32(0)
        sum_64_normal = np.float64(0)
        sum_64_descending = np.float64(0)

        for k in range(1,n[i]+1):
            if form:
                sum_32_normal += formula_sum(k,s[i])
                sum_64_normal += formula_sum(k,s[i],False)
            else:
                sum_32_normal += formula_dirichlet(k, s[i])
                sum_64_normal += formula_dirichlet(k, s[i], False)
        for k in range(n[i],0,-1):
            if form:
                sum_32_descending += formula_sum(k,s[i])
                sum_64_descending += formula_sum(k,s[i], False)
            else:
                sum_32_descending += formula_dirichlet(k, s[i])
                sum_64_descending += formula_dirichlet(k, s[i], False)
        print(f"Dla dla s = {s[i]} oraz n = {n[i]}")
        print(sum_32_normal,sum_32_descending)
        print(sum_64_normal,sum_64_descending)
        print(f"Błąd względny przód: {abs(sum_32_normal-sum_64_normal)/sum_64_normal * 100}%")
        print(f"Błąd względny tył: {abs(sum_32_descending - sum_64_descending) / sum_64_descending * 100}%")
        print("\n")
sums(False)
