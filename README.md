# ⌨️ Vim Quest

Jogo interativo de navegador para aprender **Neovim** jogando, com 12 fases que vão dos comandos mais básicos aos mais avançados.

## Como jogar

Abra o arquivo `index.html` em qualquer navegador (basta dar dois cliques nele) — não precisa instalar nada.

- Nas **fases de movimento**, leve o cursor até cada 💎 usando os comandos do Vim.
- Nas **fases de edição**, transforme o texto do editor até ficar igual ao texto objetivo.
- O contador de teclas mostra sua eficiência: tente terminar abaixo do **par** para ganhar o troféu 🏆.
- Seu progresso fica salvo no navegador (localStorage).

## Fases

| Fase | Tema | Comandos |
|------|------|----------|
| 1 | Esquerda e direita | `h` `l` |
| 2 | Cima e baixo | `j` `k` |
| 3 | Movimento livre | `hjkl` + contagem (`3j`) |
| 4 | Saltando palavras | `w` `b` `e` |
| 5 | Início e fim da linha | `0` `$` |
| 6 | Voando pelo arquivo | `gg` `G` `{n}G` |
| 7 | Caça ao caractere | `f{c}` `F{c}` `;` |
| 8 | Busca | `/texto` `n` |
| 9 | Apagando texto | `x` `dw` `dd` `u` |
| 10 | Modo de inserção | `i` `a` `A` `o` `Esc` |
| 11 | Copiar, colar e mover | `yy` `p` `dd`+`p` |
| 12 | Desafio final | `ciw` + tudo junto |

Bom treino! 🚀
