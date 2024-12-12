
![logo](/assets/imagem/chave.png)
# CutCipher 🔐

Este script utiliza a biblioteca OpenCV para identificar e desenhar contornos em uma imagem fornecida pelo usuário. Ele salva tanto a imagem com os contornos desenhados quanto uma versão contendo apenas os contornos.

---

## Funcionalidades 🔧

- **Detecção de Contornos:** Identifica os contornos em uma imagem de uma chave a partir de limiarização.
- **Geração de Imagens de Saída:**
  - Imagem original com os contornos desenhados.
  - Imagem contendo apenas os contornos.
- **Exibição Visual:** Mostra a imagem original, a imagem com contornos e a imagem apenas com os contornos em janelas separadas.

---

## Requisitos ⚙️

- Python 3.6 ou superior
- Bibliotecas:
  - OpenCV
  - NumPy

---

### Instalação das Bibliotecas 📦

Use o `pip` para instalar as dependências necessárias ou o requirements:

```bash
pip instal -r requirements.txt
```

```bash
pip install opencv-python-headless numpy
```

---

## Como Usar 🚀

1. Substitua `sua_imagem` no código pelo caminho para a imagem que deseja processar. O formato da imagem pode ser `.jpg`, `.png`, ou outros formatos suportados pelo OpenCV.
2. Execute o script:

```bash
python contornar_imagem.py
```

3. O programa processará a imagem, exibirá os resultados e salvará os arquivos no mesmo diretório do script.

---

## Saídas 📂

- **Imagem com Contornos:** `imagem_com_contornos.jpg`
- **Apenas Contornos:** `apenas_contornos.jpg`

---

## Explicação do Funcionamento 🔍

1. **Carregamento da Imagem:**
   - A imagem é carregada e convertida para tons de cinza.
2. **Limiarização (Threshold):**
   - Aplica-se um limite para destacar os elementos principais da imagem.
3. **Detecção de Contornos:**
   - Os contornos são encontrados usando `cv2.findContours`.
4. **Desenho dos Contornos:**
   - Os contornos são desenhados em uma cópia da imagem original e em uma imagem preta para gerar os dois arquivos de saída.
5. **Exibição e Salvamento:**
   - As imagens resultantes são exibidas e salvas em arquivos.

---

## Exemplo 📸

### Entrada

Imagem original:

![Imagem Original](example_original.jpg)

### Saídas

1. Imagem com contornos:

![Imagem com Contornos](example_contornos.jpg)

2. Apenas contornos:

![Apenas Contornos](example_apenas_contornos.jpg)

---

## Observações ⚠️

- Certifique-se de fornecer uma imagem de boa qualidade para resultados mais precisos.
- Este script funciona apenas para contornos externos, ignorando contornos internos.

---

## Contribuição 🤝

Sinta-se à vontade para abrir issues ou enviar PRs com melhorias no código! Estamo aceitando qualquer tipo de ajuda para fazer nosso softwares melhores. 😊

---

## AVISO ⚠️

A DEDESC está revelando a verdade, porém, não nos responsaveis pelas suas ações com nosso software, criamos com o objetivo de ajudar pessoas que trabalham com criação de chaves ou cópias de chaves quebradas.