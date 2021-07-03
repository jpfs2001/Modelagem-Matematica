from geral import Google

# matriz do exemplo
A = [
    [0, 0, 1, .5], 
    [1/3, 0, 0, 0], 
    [1/3, .5, 0, .5], 
    [1/3, .5, 0, 0]
]
# aquele valorzinho para perturbar a matriz
m = 0.15
# margem de erro considerada
margem = 0.00000001

# se chama a classe para instanciar A e m
# foi feito desse jeito para que diversos testes possam ser feitos com várias margens de erro sem que a classe precise ser chamada novamente
g = Google(A, m)

# ao se chamar o método X da classe Google, é necessário para a margem como parâmetro
# o retorno será a lista com o autovetor em cada iteração e uma lista com o respectivo erro em cada uma
# é retornado também o c, já que o pdf lá pede que ele seja impresso
[ autovetores_lista, erros_lista, c ] = g.X(margem)

print(f" Para a matriz informada, o autovetor dominante calculado é: \n {autovetores_lista[-1]} \n\n Com erro estimado em: \n {erros_lista[-1]} \n\n E a constante c para a matriz informada é: \n {c} ")
