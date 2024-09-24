# Referencias
# https://www.geeksforgeeks.org/erosion-dilation-images-using-opencv-python/
# https://es.acervolima.com/python-imagen-borrosa-usando-opencv/
# https://programmerclick.com/article/73031692994/

import cv2;
import numpy as np;

# Funciones
def visualizarImg(name):
    img = cv2.imread(name, 1);
    cv2.imshow('image', img);
    cv2.waitKey(0);
    cv2.destroyAllWindows();

def rotarImg(name, imgOriginal):
    img = cv2.imread(imgOriginal, 1);
    (h, w) = img.shape[:2];
    center = (w/2, h/2);
    angle = -15;
    scale = 1.0;
    M = cv2.getRotationMatrix2D(center, angle, scale);
    rotateImg = cv2.warpAffine(img, M, (w, h));
    cv2.imwrite(name, rotateImg);

def recortarImg(name, imgOriginal):
    img = cv2.imread(imgOriginal, 1);
    cropImg = img[90:400, 305:530];
    cv2.imwrite(name, cropImg);

def dilatarImg(name, imgOriginal):
    img = cv2.imread(imgOriginal, 1);
    mSize = (3, 3); 
    k = np.ones(mSize, np.uint8);
    dilateImg = cv2.dilate(img, k, iterations=3);
    cv2.imwrite(name, dilateImg);

def filtroOPImg(name, imgOriginal):
    img = cv2.imread(imgOriginal, 1);
    d = 9;
    sigmaColor = 75;
    sigmaSpace = 75;
    bilateralImg = cv2.bilateralFilter(img, d, sigmaColor, sigmaSpace);
    cv2.imwrite(name, bilateralImg);
   
def sobelImg(name, imgOriginal):
    img = cv2.imread(imgOriginal, cv2.IMREAD_GRAYSCALE);
    dx, dy = cv2.spatialGradient(img);
    dx = np.uint8(np.clip(dx, 0, 255));
    cv2.imwrite(name, dx);

# Definimos variables con las rutas
img = './images/examen_b.tif';
rotateImg = './images/imgRotada.tif';
cropImg = './images/imgRecortada.tif';
dilateImg = './images/imgDilatada.tif';
fOPImg = './images/imgFiltroOP.tif';
sImg = './images/imgSobel.tif';

#Orden de llamada a las funciones
sobelImg(sImg, img);
dilatarImg(dilateImg, sImg);
filtroOPImg(fOPImg, dilateImg);
rotarImg(rotateImg, fOPImg);
recortarImg(cropImg, rotateImg);
visualizarImg(cropImg);
