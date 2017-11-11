


def josefo(n,k):
    # caras = [0]*n
    # for i in range(0, n):
    #     caras[i] = i+1
    caras = list(range(1,n+1))
    i = (k - 1) % len(caras)
    caras.pop(i)
    while len(caras) > 1:
        i = (i + k - 1) % len(caras)
        caras.pop(i)
        # print(caras)
    return caras[0]



NC = int(input())
# print(NC)
for i in range(1, NC+1):
    entrada = input()
    # print(entrada)
    x = entrada.split(" ")
    n, k = x
    # print(x)
    n, k = int(n), int(k)

    result = josefo(n,k)
    print("Case "+str(i)+": "+str(result))
    # print(result)