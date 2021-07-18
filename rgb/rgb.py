import cv2

img = cv2.imread('C:/Users/jpfre/Desktop/Modelagem-Matematica/rgb/gato101.png')
(canalAzul, canalVerde, canalVermelho) = cv2.split(img)
rimage = cv2.imshow("Vermelho", canalVermelho)
gimage = cv2.imshow("Verde", canalVerde)
bimage = cv2.imshow("Azul", canalAzul)

cv2.imwrite('./rgb/r.jpg', canalVermelho)
cv2.imwrite('./rgb/g.jpg', canalVerde)
cv2.imwrite('./rgb/b.jpg', canalAzul)

cv2.waitKey(0)