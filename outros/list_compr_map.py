L1 = [2, 6, 2, 4, 6, 8, 4]
L2 = [item * 2 for item in L1]
L2
[4, 12, 4, 8, 12, 16, 8]
L1 = []
L1 = [2, 6, 2, 4, 6, 8, 4]
L2 = []
for item in L1:
    L2.append(item * 2)


def fatorial(n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n - 1)


fatorial(5)
120
fatorial(20)
2432902008176640000
L1
[2, 6, 2, 4, 6, 8, 4]
L2 = [fatorial(item) for item in L1]
L2
[2, 720, 2, 24, 720, 40320, 24]
map(fatorial, L1)
list(map(fatorial, L1))
[2, 720, 2, 24, 720, 40320, 24]
