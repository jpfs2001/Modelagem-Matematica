# neste arquivo, há um programa com interface de usuário que recebe o link de uma imagem qualquer, a redimensiona e aplica a transformação quantas vezes for desejado e com qual chave se desejar
# se não for inserido link, será utilizado o do gatinho mega feliz
# se não for inserida chave, será utilizada a padrão
# se na chave se digitar "gato", se utilizará a que foi passada para o outro grupo

from geral import funcoesProntas
from PIL import Image
import numpy as np
import os
import requests

# salva imagem de link no diretorio
def capturarImagemOnline(link):
    print('\nbaixando imagem.....')
    page = requests.get(link)
    f_ext = os.path.splitext(link)[-1]
    f_name = f'./figs/temp/tempImg{f_ext}'
    with open(f_name, 'wb') as f:
        f.write(page.content)

# redimensiona imagem
def redimensionarImagem(link):
    print('redimensionando.....')
    # abre a imagem
    im = Image.open(link)
    # redimensiona conforme o tamanho
    t = 101,101
    im = im.resize(t, Image.NEAREST)
    # salva
    im.save('./figs/temp/redimensionado.jpg', 'JPEG')
    # apaga a imagem temporária
    os.remove('./figs/temp/tempImg.jpg')
    print('imagem redimensionada!\n')

def interrogacao():
    # pede pelo link
    link = input('-> Insira o link da imagem (se deixar vazio, será usada a de exemplo):\n')
    # se for vazio
    if link == "":
        link = 'https://aloaloaloalo.000webhostapp.com/imagem/gatofeliz.jpg'
        print('*Usando a imagem padrão*')
    # salva a imagem de forma provisória
    capturarImagemOnline(link)
    # redimensiona a imagem
    redimensionarImagem('./figs/temp/tempImg.jpg')

    chave = input('-> Qual chave deseja utilizar?\nPor exemplo, a chave no formato\n [a b]\n [c d]\ndeve ser inserida no formato: a, b, c, d\nDeixe vazio para usar a padrão (1,1,1,2)\n')
    if chave == "": 
        chave = "1,1,1,2"
        print('*Usando a chave padrão*\n')
    elif chave == "gato":
        chave = "18,13,11,8"
        
    chave = chave.split(',')
    C = [[int(chave[0]), int(chave[1])],[int(chave[2]), int(chave[3])]]

    qualIt = int(input('-> Em qual iteração deseja encerrar o processo? \n'))

    salvarCadaIteracao = input('-> Deseja salvar todas as iterações? (s/n) \n')

    if salvarCadaIteracao == 's':
        salvarCadaIteracao = True
    elif salvarCadaIteracao == 'n':
        salvarCadaIteracao = False
    
    salvarTxt = input('-> Deseja salvar cada matriz em txt? (s/n) \n')
    if salvarTxt == 's': salvarTxt = True
    elif salvarTxt == 'n': salvarTxt = False

    # aplica a função gama
    funcoesProntas.gerarMatrizesDeImagemPropria(C, './figs/temp/redimensionado.jpg', qualIt, salvarCadaIteracao, salvarTxt)

    print('pronto!\nResultado salvo na pasta "resultado"')

    # apaga a imagem temporária
    os.remove('./figs/temp/redimensionado.jpg')
    # exibe a transformada
    Image.open(f'./resultado/mistura.png').show()

interrogacao()

# link de exemplo
# https://aloaloaloalo.000webhostapp.com/imagem/dara.jpg


