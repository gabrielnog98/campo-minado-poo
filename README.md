# Campo Minado em Python

Projeto desenvolvido em **Python** com **Pygame**, recriando o clássico jogo **Campo Minado** com interface gráfica, menu inicial, tela de configurações e sistema de vitória e derrota.

## Sobre o projeto

O jogo permite ao jogador personalizar a partida antes de iniciar, ajustando:

- número de linhas
- número de colunas
- quantidade de minas

Durante a execução, o jogador pode revelar células, marcar bandeiras e tentar limpar o tabuleiro sem acionar nenhuma bomba.

## Funcionalidades

- Interface gráfica com Pygame
- Menu inicial
- Tela de configurações da partida
- Ajuste de linhas e colunas do tabuleiro
- Ajuste da quantidade de minas
- Revelação automática de áreas vazias
- Sistema de bandeiras
- Tela de vitória
- Tela de derrota
- Uso de imagens para bomba, explosão e bandeira

## Tecnologias utilizadas

- Python
- Pygame

## Estrutura do projeto

```bash
campo-minado-poo/
├── main.py
├── game.py
├── models.py
├── screens.py
├── assets.py
├── settings.py
├── Imagens/
│   ├── bomba.png
│   ├── explosao.png
│   └── flag.png
└── .gitignore
```

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/gabrielnog98/campo-minado-poo
cd campo-minado-poo
```

### 2. Instale as dependências

```bash
pip install pygame
```

### 3. Execute o projeto

```bash
python main.py
```

## Controles

### Menu inicial

- **Enter**: acessar configurações

### Tela de configurações

- **W / S**: aumentar ou diminuir o número de linhas
- **A / D**: aumentar ou diminuir o número de colunas
- **+ / -**: aumentar ou diminuir a quantidade de minas
- **Enter**: iniciar partida

### Durante o jogo

- **Clique esquerdo do mouse**: revelar célula
- **Clique direito do mouse**: colocar ou remover bandeira

### Tela final

- **Enter**: reiniciar e voltar para as configurações

## Configurações padrão

O projeto inicia com os seguintes valores padrão:

- **20 linhas**
- **20 colunas**
- **40 minas**

## Organização do código

- **main.py**: controla o fluxo principal da aplicação e os estados do jogo
- **game.py**: gerencia a lógica geral da partida
- **models.py**: define as classes do tabuleiro e das células
- **screens.py**: renderiza as telas do sistema
- **assets.py**: carrega imagens e fontes
- **settings.py**: armazena constantes e configurações padrão

## Objetivo acadêmico

Este projeto representa uma implementação orientada a objetos do jogo Campo Minado, explorando conceitos como:

- modularização
- organização em classes
- manipulação de eventos
- interface gráfica
- lógica de jogo

## Melhorias futuras

- contador de tempo
- contador de bandeiras restantes
- níveis de dificuldade predefinidos
- botão de reinício dentro da partida
- proteção para o primeiro clique nunca ser uma bomba
- ranking de melhores tempos

## Autor

Desenvolvido para fins acadêmicos e de estudo, com foco em programação orientada a objetos e desenvolvimento de jogos em Python.
