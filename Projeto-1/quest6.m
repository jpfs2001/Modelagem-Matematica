## começa o programa limpando as variaveis
clear

## Variavel g

g = [0.28; 0.31; 0.25; 0.23; 0.37];

##variavel auxiliar, que guardara o inverso do g

aux = [1/g(1,1); 1/g(2,1); 1/g(3,1); 1/g(4,1); 1/g(5,1)];

## Variavel p

p = [0; 50; 100; 150; 200; 250];

## resolvendo a inequação

resultado = (p(3,1)/(aux(1,1) + aux(2,1))) * (aux(1,1) + aux(2,1) + aux(3,1) + aux(4,1))  ;

## retornando o resultado

printf("Para p5 ser maior retorno sustentavel, temos  p5 > %.2f", resultado);
