"""
Run Test
Writer: Sagor Sarker
Steps: 
* Calculate ups and downs of value, a = total number
* Calculate Mean = (2*n-1)/3 here n is total random number
* Calculate Variance = sqrt((16*n-29)/90)
* calculate z = (a-mean)/variance
* z_alpha
if z<z_alpha and z>(-z_alpha) then accepted,
else: rejected

"""

from itertools import groupby
import math

def run_test(r_list):
    r_seq = []

    for i, j in zip(r, r[1:]):
#         print(i, j)
        if i<j:
            r_seq.append(1)
        else:
            r_seq.append(0)
    print(r_seq)
    a = [len(list(group)) for key, group in groupby(r_seq)]
    return len(a)

def mean(n):
    mean = (2*n - 1)/3
    return mean
def var(n):
    var = math.sqrt((16*n-29)/90)
    return var

if __name__=="__main__":
    r = [0.41, 0.68, 0.89, 0.84, 0.74, 0.91, 0.55, 0.71, 0.36, 0.30,
        0.09, 0.72, 0.86, 0.08, 0.54, 0.02, 0.11, 0.29, 0.16, 0.18,
        0.88, 0.91, 0.95, 0.69, 0.09, 0.38, 0.23, 0.32, 0.91, 0.53,
        0.31, 0.42, 0.73, 0.12, 0.74, 0.45, 0.13, 0.47, 0.58, 0.29]
# #     r = [0.41, 0.68, 0.89, 0.84, 0.74, 0.91, 0.55, 0.71, 0.36, 0.30]
    n = len(r)
    a = run_test(r)
    mean = mean(n)
    var = var(n)
    z = (a - mean)/var
    z_alpha = 1.96
    if z<z_alpha and z>(-z_alpha):
        print('Accepted')
    else:
        print('Rejected!')
    