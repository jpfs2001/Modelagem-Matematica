from geral import Google
from grafo import desenhaA
from matrizA import insercaoDoUsuario

# menu

print("Vamos definir a matriz de ligação A de acordo com o problema = que se deseja explorar:")
print("1 - Exemplo do enunciado, com 4 páginas.")
print("2 - Exemplo do Exercício 3, com 8 páginas.")
print("3 - Criar novo exemplo.")
x = int(input("Digite a opção correspondente: "))

if x == 1:
    A = [
       [0, 0, 1, .5], 
       [1/3, 0, 0, 0], 
       [1/3, .5, 0, .5], 
       [1/3, .5, 0, 0]
       ]
elif x == 2:
    A = [
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5],
        [0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5],
        [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.5, 0.5, 1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.5, 0.0, 0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]
        ]
elif x == 3:
    A = insercaoDoUsuario()

# matriz do exemplo
# exemplo 1
# A = [
#     [0, 0, 1, .5], 
#     [1/3, 0, 0, 0], 
#     [1/3, .5, 0, .5], 
#     [1/3, .5, 0, 0]
# ]

# aquele valorzinho para perturbar a matriz
m = 0.15
# margem de erro considerada
margem = 10**(-5)

# ---- Cálculos ---- #
# chama-se a classe para instanciar A e m
# foi feito desse jeito para que diversos testes possam ser feitos com várias margens de erro sem que a classe precise ser chamada novamente
g = Google(A, m)

# ao se chamar o método X da classe Google, é necessário para a margem como parâmetro
# o retorno será a lista com o autovetor em cada iteração e uma lista com o respectivo erro em cada uma
# é retornado também o c, já que o pdf lá pede que ele seja impresso
[ autovetores_lista, erros_lista, c ] = g.X(margem)

# ---- Exibição ---- #
# autovetores
print(f"Para a matriz informada, o autovetor dominante calculado é: \n {autovetores_lista[-1]} \n\nCom erro estimado em: \n {erros_lista[-1]} \n\nE a constante c para a matriz informada é: \n {c} ")

# desenha matriz A
desenhaA(A)