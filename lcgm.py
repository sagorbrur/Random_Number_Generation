# Random Number Generation
# Linear Congruential Method

def lcg(a, constant , mod):
    lcg.seed = (a*lcg.seed + constant) % mod
#     x1 = (x0*a+c)%m
    return lcg.seed/mod

lcg.seed = int(input("Enter the seed(x_0) : "))
a = int(input('Enter a: '))
c = int(input('Enter c: '))
mod = int(input('Enter mod: '))


for i in range(10):
    print(lcg(a, c, mod))