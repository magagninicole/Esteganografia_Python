#M2.2 - INTRODUÇÃO A PROGRAMAÇÃO EM PYTHON 
#ALUNOS: JOÃO VITOR SPECHT KOGUT E NICOLE MAGAGNIN

from matplotlib import image
import numpy as np
import cv2
from matplotlib import pyplot as plt 


######
IMAGE_PATH = "lenna.png"
######

def array_reds_originais(imagem):
    imagem = imagem
    img_shape = imagem.shape
    img_X = img_shape[0] #separa x e y da imagem
    img_Y = img_shape[1]

    bits_vermelhos_originais = [] #cria vetor que pega bits vermelhos

    for y in range(img_Y):
        for x in range(img_X):
            pixel_atual = imagem[x,y] #pixel atual igual a imagem em x e y
            red = pixel_atual[2] % 2 # impares sao 1
            bits_vermelhos_originais.append(red) # montagem de 0 e 1s originais da imagem
    return bits_vermelhos_originais #retorna bits vermelhos originais

def insere_mensagem(imagem, bits):
    imagem = imagem
    img_shape = imagem.shape
    img_X = img_shape[0]
    img_Y = img_shape[1]

    for y in range(img_Y):
        for x in range(img_X):
            pixel_atual = imagem[x,y]
            if bits[(y*img_X) + x] != (pixel_atual[2] % 2): #Posiciona os bits na imagem
                if pixel_atual[2] != 255: #Se nao for o último, coloca na proxima posicao
                    pixel_atual[2] = pixel_atual[2] + 1
                else:
                    pixel_atual[2] = pixel_atual[2] - 1 #senao na atual
                imagem[x,y] = pixel_atual

    return imagem

def bitfield(n):
    return [int(digit) for digit in bin(n)[2:]]

def gerar_mensagem(mensagem): #Gera mensagem binaria
    lista = []
    for m in mensagem:
        val = ord(m)
        bits = bitfield(val)

        if len(bits) < 8:
            for a in range(8-len(bits)):
                bits.insert(0,0)
        lista.append(bits)
    arr = np.array(lista)
    arr = arr.flatten()
    return arr


def converter_mensagem(saida): #Converte para leitura
    bits = np.array(saida)
    mensagem_out = ''
    bits = bits.reshape((int(len(saida)/8), 8))
    for b in bits:
        sum = 0
        for i in range(8):
            sum += b[i]*(2**(7-i))
        mensagem_out += chr(sum)
    return mensagem_out

#cada imagem e um vetor de vetores 
#openCV utiliza o padrão BGR para definir a definicao dos pixels

escolha = 0

while escolha != 3:
    print("1 - INSERIR MENSAGEM\n2 - LER MENSAGEM\n3- PARAR PROGRAMA")
    escolha = int(input())
    if escolha == 1:
        imagem = cv2.imread(IMAGE_PATH)
        bits_vermelhos_originais = array_reds_originais(imagem)

        print("INSIRA A FRASE A SER ESCONDIDA: ")
        frase_inserida = input()
        frase_inserida = gerar_mensagem(frase_inserida)

        for i in range(len(frase_inserida)):
            bits_vermelhos_originais[i] = frase_inserida[i]

        imagem_modificada = insere_mensagem(imagem,bits_vermelhos_originais)
        cv2.imwrite("modificada.png", imagem_modificada)
    elif escolha == 2:
        print("INSIRA O NOME DO ARQUIVO COM EXTENSAO: ")
        filepath = input()
        imagem = cv2.imread(filepath)
        bits_vermelhos_originais = array_reds_originais(imagem)
        mensagem = converter_mensagem(bits_vermelhos_originais)
        print("QUANTOS CARACTERES IMPRIMIR?:")
        limite = int(input())
        print(mensagem[: limite])