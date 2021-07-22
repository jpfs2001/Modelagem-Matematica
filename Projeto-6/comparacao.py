# a função aqui presente compara o histograma de duas imagens
import imgcompare

def comparar(img1, img2):
    dif = imgcompare.image_diff_percent(f'./figs/{img1}.png', f'./figs/{img2}.png')
    return dif