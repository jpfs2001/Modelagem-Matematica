# há uma classe no geral.py que contém algumas funções prontas, como é o caso da tarefa de decifrar a imagem se utilizando dos arquivos de texto oferecidos e dispostos na pasta "tarefa"
# basicamente, a chave utilizada é a primeira possível ([[1, 1],[1, 2]]
# nas variáveis R, G e B são alocadas as matrizes já formatadas presentes nos três arquivos de texto
# a variável limIt, tendo seu valor como 60, determina que o limite de iterações será 60 (para o caso de alguma coisa dar errado no processo e o programa não começar a fazer cálculos absurdos)
# a variável qualIteracao determina que a iteração a ter suas matrizes mescladas em uma única imagem colorida, e nesse caso é a sexta iteração
 # passar True como parâmetro no método arnoldTarefa() indica que todo o procesos será salvo. Se não for esse o objetivo, só será salva a mistura colorida.

from geral import funcoesProntas

funcoesProntas().arnoldTarefa(True)