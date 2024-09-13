# Projeto de Monitoramento de Câmeras - Prefeitura de São João del-Rei

Este repositório contém uma solução para o problema de posicionamento de câmeras de vigilância na região central da cidade de São João del-Rei, com o objetivo de monitorar todas as ruas com o menor número possível de câmeras.

## Descrição do Problema

A Prefeitura de São João del-Rei contratou uma empresa para projetar um sistema de vigilância por câmeras no centro da cidade, especificamente em um raio de 1km do Campus Santo Antônio da UFSJ. O objetivo é posicionar câmeras em esquinas de forma a cobrir todas as ruas da região.

Para modelar o problema, a cidade foi representada como um grafo onde:
- **Vértices**: Representam as esquinas.
- **Arestas**: Representam as ruas.

Cada câmera posicionada em uma esquina monitora todas as ruas conectadas a essa esquina.

## Objetivo

O objetivo é encontrar a cobertura mínima de câmeras necessária para monitorar todas as ruas da região. A solução deve indicar quais esquinas terão câmeras e quais ruas serão monitoradas por cada câmera.

## Arquivos

- **`sjdr.gml`**: Arquivo contendo a representação do grafo da região de interesse.
- **`monitoramento.py`**: Script para encontrar a cobertura mínima do grafo.

## Como Executar

1. **Pré-requisitos**:
   - Python 3.x
   - Bibliotecas Python: `networkx`, `scipy`

   Você pode instalar as bibliotecas necessárias usando pip:
   ```bash
   pip install networkx scipy

2. **Executar o Código:**

    - Navegue até o diretório onde se encontram os arquivos e execute o script Python:

    - /bin/python monitoramento.py