# A DEDESC está revelando a verdade, porém, não nos responsaveis pelas suas ações com nosso software,
# criamos com o objetivo de ajudar pessoas que trabalham com criação de chaves ou cópias de chaves 
# quebradas.

import cv2
import numpy as np

def contornar_imagem(caminho_imagem):
    # Carregar a imagem
    imagem = cv2.imread(caminho_imagem)
    if imagem is None:
        print("Erro: Não foi possível carregar a imagem.")
        return

    # Converter a imagem para tons de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aplicar o método de limiarização (threshold)
    _, limiarizada = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

    # Encontrar contornos
    contornos, _ = cv2.findContours(limiarizada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Desenhar contornos na imagem original
    imagem_com_contornos = imagem.copy()
    cv2.drawContours(imagem_com_contornos, contornos, -1, (0, 255, 0), 2)

    # Criar uma imagem vazia para desenhar apenas os contornos
    apenas_contornos = np.zeros_like(imagem_cinza)
    cv2.drawContours(apenas_contornos, contornos, -1, 255, 1)

    # Salvar a imagem com contornos
    caminho_saida_contornos = "imagem_com_contornos.jpg"
    cv2.imwrite(caminho_saida_contornos, imagem_com_contornos)
    print(f"Imagem com contornos salva como: {caminho_saida_contornos}")

    # Salvar a imagem apenas com os contornos
    caminho_saida_apenas_contornos = "apenas_contornos.jpg"
    cv2.imwrite(caminho_saida_apenas_contornos, apenas_contornos)
    print(f"Imagem apenas com os contornos salva como: {caminho_saida_apenas_contornos}")

    # Exibir a imagem original, a imagem com contornos e apenas os contornos
    cv2.imshow('Imagem Original', imagem)
    cv2.imshow('Contornos', imagem_com_contornos)
    cv2.imshow('Apenas Contornos', apenas_contornos)

    # Aguardar o usuário pressionar uma tecla e fechar as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Substitua 'sua_imagem.jpg' pelo caminho da sua imagem
contornar_imagem('sua_imagem')
