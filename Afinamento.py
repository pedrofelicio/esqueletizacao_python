import cv2
import numpy as np

def conectividade(img,pts):
    cont=0
    for p in range(1,8,1):
        if(img[pts[p][0]][pts[p][1]]>127 and img[pts[p+1][0]][pts[p+1][1]]<127):
            cont+=1
    if(cont == 1):
        return True
    return False

def PixelsPretos(img,pts):
    cont=0
    for p in range(1,9,1):
        if(img[pts[p][0]][pts[p][1]]<127):
            cont+=1
    if(cont>=2 and cont<=6):
        return True
    return False

def BrancoP2P4P8(img,pts):
    if(img[pts[1][0]][pts[1][1]]>127 or img[pts[3][0]][pts[3][1]]>127 or img[pts[7][0]][pts[7][1]]>127):
        return True
    return False

def BrancoP2P6P8(img,pts):
    if(img[pts[1][0]] [pts[1][1]]<127 or img[pts[5][0]][pts[5][1]]<127 or img[pts[7][0]][pts[7][1]]<127):
        return True
    return False
    
def BrancoP2P4P6(img,pts):
    if(img[pts[1][0]][pts[1][1]] < 127 or img[pts[3][0]][pts[3][1]] < 127 or img[pts[5][0]][pts[5][1]] < 127 ):
        return True
    return False    


def BrancoP4P6P8(img,pts):
    if(img[pts[7][0]][pts[7][1]]>127 or img[pts[5][0]][pts[5][1]]>127 or img[pts[3][0]][pts[3][1]]>127):
        return True
    return False

def PretoBranco(img):
    
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    lin, col = img.shape
    img2 = np.zeros((lin,col,1), dtype=np.uint8)
    for i in range(lin):
        for j in range(col):
            if img[i][j] < 180:
                img2[i][j] = 0
            else:
                img2[i][j] = 255

    return img2



def afinador(img):
    linha,coluna,_ = img.shape
    cont=1
    flag = True
    while(cont>0):
        cont=0
        excluidos=[]
        for i in range(1,linha-1,1):
            for j in range(1,coluna-1,1):
                pts = np.zeros((9,2),dtype=int)
                pts[0][0]=i,pts[0][1]=j,pts[1][0]=i-1,pts[1][1]=j,pts[2][0]=i-1,pts[2][1]=j+1
                pts[3][0]=i,pts[3][1]=j+1,pts[4][0]=i+1,pts[4][1]=j+1,pts[5][0]=i+1,pts[5][1]=j
                pts[6][0]=i+1,pts[6][1]=j-1,pts[7][0]=i,pts[7][1]=j-1,pts[8][0]=i-1, pts[8][1]=j-1
                if(img[i][j]<127):
                    if(conectividade(img,pts) and PixelsPretos(img,pts)):
                        if(flag):
                            if(BrancoP2P4P8(img,pts) and BrancoP2P6P8(img,pts)):
                                excluidos.append([i,j])
                                cont+=1
                        else:
                            if(BrancoP2P4P6(img,pts) and BrancoP4P6P8(img,pts)):
                                excluidos.append([i,j])
                                cont+=1
        for i in range(len(excluidos)):
            img[excluidos[i][0]][excluidos[i][1]]=255
            flag = not flag
    return img

#SÓ POR A IMAGEM.
img= cv2.imread("letraforma.jpg")
imgPreta=PretoBranco(img)
cv2.imshow("preta",imgPreta)
cv2.imshow("afinador",afinador(imgPreta))
cv2.waitKey(0)

        
        
        