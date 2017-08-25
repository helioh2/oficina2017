'''
PROBLEMA:

Projete um programa de editor de texto simples (de uma linha).
O programa deve permitir que o usuário digite com o teclado, dando feedback imediato na tela.
Deve permitir, também, que o usuário conserte seu texto por meio da tecla 'backspace' (tecla de apagar texto).

DICA1: Muita atenção na análise de domínio. Uma análise bem feita facilitará o desenvolvimento.
DICA2: o valor referente à tecla 'backspace' é pg.K_BACKSPACE, e para as letras do alfabeto é, pg.K_a, pg.K_b, pg.K_c,
        e assim por diante.
DICA3: veja como desenhar texto na tela no exemplo contagem_regressiva.py.
       Use sabiamente as constantes (se fez analise de dominio bem feita, isso torna-se natural).
DICA4: use 'nome_variavel[:-1]' para pegar o texto sem a última letra
DICA5: verifique o que acontece quando tenta dar 'backspace' em um texto vazio (pode ser necessário usar (if ...) )
DICA6: use concatenação de strings
        para inserir uma nova letra no final do texto (ex: nome_variavel+"a"). Para transformar o 
        valor da tecla em string (ex: pg.K_a -> "a"), use: chr(pg.K_a)
DICA7: este programa não precisa de 'quando_tick=...'. Por quê?

NÃO ESQUEÇAM QUE TODAS AS RECEITAS DEVEM SER UTILIZADAS, ASSIM COMO OS TEMPLATES APROPRIADOS!!

'''