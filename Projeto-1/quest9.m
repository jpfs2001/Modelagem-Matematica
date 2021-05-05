## Começa o código limpando as variaveis
clear

## Variavel preço (começa como 0 porque muda não tem preço)
p = [0];

## Variavel de crescimento
g = [];

## Variavel quantidade de árvores
s = input("Digite a quantidade de árvores: ");

## Variavel contendo o valor máximo de cada classe
ret = [0];

## Variavel referente a quantidade de classes
n = input("Digite a quantidade de classes: ");

## Variavel para auxiliar
aux = [];
aux2 = [];

## Variavel com valor máximo
max = [0];

## Variavel para auxiliar na somatoria
sum = [0];
 
## Estrutura de repetição para ler os valores de p
for i = 2:n
  fprintf("Digite o valor de p%d: ", i);
  aux = input("");
  p = [p; aux];
endfor

## Estrutura de repetição para ler os valores de g
for i = 1:(n-1)
  fprintf("Digite o valor de g%d: ", i);
  aux = input("");
  g = [g; aux];
endfor

f = [g; 0];

## Estrutura de repetição para fazer o calculo do valor
for i = 2:n
  sum = 0;
  ## Estrtutura de repetição dentro de outra estrutura de repetição para calcular a somatoria
  for j = 1:(i-1)
    sum = sum + 1/(g(j,1));
  endfor
  
  ##calculando o valor otimo sustentavel da classe i
  aux = p(i, 1)/sum;
  
  ret = [ret; aux*s];
  
  ## Estrutura de decisão para descobrir qual o maior número
  if(aux > max)
    max = aux;
    aux2 = i;
   endif
endfor  

## Comando para mostrar o resultado
fprintf("A maior valor  é de %.2f e é da classe %d", max*s, aux2);
  
 ## Mostrando o valor sustentavel otimo de cada classe em um grafico de barras
 
 bar(ret);
 title("Retorno sustentável ótimo de cada classe");
 xlabel("Classe");
 ylabel('Retorno [s*R$]');
 
 
 
  

