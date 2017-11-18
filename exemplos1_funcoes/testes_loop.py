


# nums = [5, 6, 7, 8, 10, -38, 27, -2]

# for n in nums:
#   if n < 0:
#     print(n)
#     break



# for n in nums:
#   if n < 0:
#     print(n*2)


# for letter in 'Django':     # First
#   if letter == 'D':
#       continue
#   print('Current Letter:', letter)



'''primo: Numero -> Boolean'''
def primo(n):
    k = n//2
    eh_primo = True
    while k > 1:
      if n % k == 0:
          # print("nao eh primo")
          eh_primo = False
          break
      k -= 1
    return eh_primo

print(primo(17))

'''Numero -> List<Numero>'''
def todos_primos_ate(x):
    primos = []
    for k in range(2,x+1):
        if primo(k):
            primos.append(k)
    return primos

import time
t_inicial = time.time()
print(todos_primos_ate(100000))
t_final = time.time()
t_total = t_final - t_inicial
print(t_total)







