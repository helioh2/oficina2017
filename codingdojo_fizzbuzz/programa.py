'''
Função -> int número
retorna > "fiz" || "buss" || "fizbuss" || int número

'''

def fizbuss(numero):
    if numero %3 == 0 and numero %5 == 0:
        return "fizbuss"
    if numero %3 == 0:
        return "fiz"
    if numero % 5 == 0:
        return "buss"
    else:
        return numero




assert fizbuss(3)=="fiz"
assert fizbuss(5)=="buss"
assert fizbuss(4)==4
assert fizbuss(15)=="fizbuss"



n = 0
while (n < 2000000):
    print (fizbuss(n))
    n += 1
