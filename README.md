# ⌨️ Vim Quest

Jogo interativo de navegador para aprender **Neovim** jogando — estrutura de capítulos e missões, desafios que combinam comandos, sistema de estrelas por eficiência e um modo Arena contra o relógio.

## Como jogar

Abra o arquivo `index.html` em qualquer navegador (basta dar dois cliques) — não precisa instalar nada.

- Cada **missão** tem vários desafios em sequência, misturando os comandos aprendidos.
- Nos desafios de **movimento**, leve o cursor até cada 💎.
- Nos desafios de **edição**, transforme o texto até ficar igual ao objetivo.
- Termine a missão com poucas teclas para ganhar até **⭐⭐⭐** (o "par" é a meta de 3 estrelas).
- Missões desbloqueiam em sequência e o progresso fica salvo no navegador (localStorage).

## Estrutura

### Capítulo 1 · Movimento
| Missão | Comandos |
|--------|----------|
| 1.1 Primeiros Passos | `h j k l` + contagens (`5l`, `3j`) |
| 1.2 Palavras e Extremos | `w` `b` `e` `0` `^` `$` |
| 1.3 Saltos e Caça | `gg` `G` `{n}G` `f` `t` `F` `T` `;` |
| 1.4 Radar de Busca | `/texto` `n` `N` + revisão geral |

### Capítulo 2 · Edição
| Missão | Comandos |
|--------|----------|
| 2.1 Cirurgia de Precisão | `x` `r{c}` `~` `u` |
| 2.2 O Operador d | `dw` `D` `dd` `2dd` `J` |
| 2.3 Inserção Total | `i` `a` `I` `A` `o` `O` `Esc` |
| 2.4 Change & Undo | `cw` `ciw` `u` `Ctrl+r` |
| 2.5 Copiar & Colar | `yy` `p` `P` `dd`+`p` `yw` |

### Capítulo 3 · Avançado
| Missão | Comandos |
|--------|----------|
| 3.1 Text Objects | `ci"` `ci(` `ci{` `ci[` `di…` |
| 3.2 Modo Visual | `v` `V` + `d` `y` `c` |
| 3.3 Desafio do Mestre | tudo junto, refatorações reais |

### 🏟️ Arena
Drills aleatórios (movimento + edição) contra o relógio: você começa com 60 segundos e cada desafio completado adiciona +5s ao cronômetro — sobreviva o máximo que conseguir. O recorde fica salvo.

## Desenvolvimento

O jogo é um único arquivo `index.html` sem dependências, com um mini-motor Vim em JavaScript (modos normal/inserção/visual/busca, operadores, text objects, registradores e undo/redo).

Bom treino! 🚀
