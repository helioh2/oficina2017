
def contagem_regressiva():
      for k in range(10,-1,-1):
            print(k)

def contagem_regressiva_rec(k):
      print(k)
      if k > 0:
            contagem_regressiva_rec(k-1)


#main:            
contagem_regressiva_rec(10)
