
"""
Kolmogrov Smirnov Test
writer: Sagor Sarker
PDF page 306
Steps: 
* Ri(Random Numbers) [0.05, 0.14, 0.44, 0.81, 0.93]
* i/N
* D+(max) = max(i/N-Ri)
* D-(max) = max(Ri-((i-1)/N))
* D = max(D+(max), D-(max))
* D_alpha
* if D>D_alpha , null hypothesis rejected
   else: accepted

"""


def ksft(r):
    i_n = []
    r_len = len(r)
    for i,j in enumerate(r):
        m = (i+1)/r_len # i/N
        i_n.append(m)

    d_plus = [x1 - x2 for (x1, x2) in zip(i_n, r)]
    print(d_plus)
    d_plus_max = max(d_plus)
    print(d_plus_max)

    d_minus = [x1-(i/r_len) for i, x1 in enumerate(r)]
    print(d_minus)
    d_minus_max = max(d_minus)
    print(d_minus_max)
    d = max(d_plus_max,d_minus_max)
    print(d)
    return d

if __name__=="__main__":
    
    N = int(input('Enter N: ')) # 5
    r = [] 
    for i in range(N):
        x = float(input()) # 0.05, 0.14, 0.44, 0.81, 0.93
        r.append(x)
    
    d = ksft(r)
    
    d_alpha = 0.565
    
    if d>d_alpha:
        print('Rejected!')
    else:
        print('Accepted!')


# Result is Accepted for give example
