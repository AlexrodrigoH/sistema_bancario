# Sistema Bancário

Projeto desenvolvido para estudo e prática de Python.

O sistema começou com conceitos básicos de programação procedural e está
sendo ampliado gradualmente conforme novos conceitos são estudados.

O objetivo não é apenas construir um sistema bancário, mas utilizar o projeto
como ambiente prático para aprender programação, organização de código,
Git/GitHub e, futuramente, Programação Orientada a Objetos.

## Funcionalidades atuais

- Cadastro de clientes
- Pesquisa de clientes por nome
- Pesquisa de clientes por índice
- Listagem de clientes cadastrados
- Depósitos
- Saques
- Consulta de extrato
- Registro de data e hora das movimentações
- Persistência dos dados dos clientes em arquivos

## Estrutura atual

O projeto utiliza módulos separados para dividir algumas responsabilidades:

- `banco_main.py` — fluxo principal do sistema
- `opcoes_menu.py` — tratamento das opções e operações do menu
- `adicionar_clientes.py` — operações relacionadas aos dados dos clientes
- `valida_entrada.py` — validações de entrada

Os dados gerados durante a execução são armazenados localmente no diretório
`clientes/` e não são versionados pelo Git.

## Conceitos praticados

Durante o desenvolvimento estou praticando conceitos como:

- Variáveis e tipos de dados
- Condicionais
- Laços de repetição
- Funções e retorno de valores
- Listas
- Manipulação de strings
- Manipulação de arquivos
- Módulos
- Tratamento de erros
- Validação de entradas
- Git e GitHub
- Branches e Pull Requests
- Integração Contínua com GitHub Actions

## Desenvolvimento

O projeto está em desenvolvimento e novas funcionalidades são adicionadas
conforme avanço nos estudos.

A implementação atual ainda é predominantemente procedural.

A Programação Orientada a Objetos será introduzida posteriormente, quando
os problemas encontrados na estrutura procedural justificarem essa mudança.

## Status

Em desenvolvimento.