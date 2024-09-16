import cv2 as cv
import pytesseract as tes

img = cv.imread(r'nivus_e_t-cross.jpg')

cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('cinza', cinza)

_, bin = cv.threshold(cinza, 146, 255, cv.THRESH_BINARY_INV)
#cv.imshow('bin', bin)

#edge = cv.Canny(bin, 150, 255)
edge = cv.GaussianBlur(bin, (3, 1), 1)
#cv.imshow('Desfoque', edge)

contornos, _= cv.findContours(edge, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
placas = list()
cont = 0
for c in contornos:
    perimetro = cv.arcLength(c, True)
    
    if 290>perimetro>220 :
        aprox = cv.approxPolyDP(c, 0.03 * perimetro, True)
        if len(aprox) == 4:
            x, y, alt, lar=cv.boundingRect(c)
            cv.rectangle(img, (x, y), (x+alt, y+lar), (0, 255, 0), 1)
            placas.append(img[y:y+lar, x:x+alt])
            cv.imshow(f"Placa{cont}",img[y:y+lar, x:x+alt])
            cont+=1

for placa in placas:
    texto_placa = tes.image_to_string(placa, config='--psm 8')
    print("Placa detectada:", texto_placa)

cv.imshow('draw', img)
cv.waitKey(0)
cv.destroyAllWindows()