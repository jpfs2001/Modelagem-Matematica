## Começa o código limpando as variaveis
clear;
## Variavel preço (começa como 0 porque muda não tem preço)
p = [0];

## Variavel de crescimento
g = [];


## Variavel contendo o valor máximo de cada classe
ret = [0];

## Variavel referente a quantidade de classes
n = input("Digite a quantidade de classes: ");

## Variavel para auxiliar
aux = [];

## Variavel com valor máximo
max = [0];

## Variavel para auxiliar na somatoria
sum = [0];
 
## Variavel com a classe com maior retorno sustentavl
k = 0;

## Algoritmo para calcular RT
 
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
  
  ret = [ret; aux];
  
  ## Estrutura de decisão para descobrir qual o maior número
  if(aux > max)
    max = aux;
    k = i;
   endif
endfor  


## Algoritmo para calcular quantas arvores vão ser retiradas

## Variavel quantidade de árvores. s = 1 para mostrar y em função de s
s = 1;

## Somatoria dos inversos de g
sum = 0;

for i = 1:(k-1)
  sum += 1/g(i,1);
endfor

y = s/sum;

## Retorna quantas arvores serão retiradas por ciclo
  
fprintf("Serão retiradas %f * s árvores por ciclo.\n", y);




