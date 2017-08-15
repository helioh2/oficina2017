print(1+2+3)
print("ola mundo")


n = 10   ## atribuição de variável
print(type(n))

n1 = 21  ##reatribuição / atualização

n2 = 2525  #variavel global
print(n2)


def eh_par_ou_impar(n):
      x = 5   #variavel local
      print(x)  #imprime var local
      print(n1)  #imprime var global
      if n % 2 == 0:
            print('par')
      else:
            print('impar') 

#print(x)   não dá certo

#exemplo:
eh_par_ou_impar(5)  # -> "impar"
eh_par_ou_impar(6)  # -> "par"




      
      

      


