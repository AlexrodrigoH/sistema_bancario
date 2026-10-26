# Sistema Bancário

Projeto desenvolvido para estudo e prática de Python.

O sistema começou com conceitos básicos de programação procedural e está sendo ampliado gradualmente conforme novos conceitos são estudados.

O objetivo não é apenas construir um sistema bancário, mas utilizar o projeto como ambiente prático para aprender programação, organização de código, Git/GitHub e Programação Orientada a Objetos (POO).

## Funcionalidades atuais

- Cadastro de clientes
- Pesquisa de clientes por nome
- Pesquisa de clientes por índice
- Listagem de clientes cadastrados
- Depósitos
- Saques
- Consulta de extrato
- Registro de data e hora das movimentações
- Persistência dos dados dos clientes em arquivo JSON
- Validação de nomes, incluindo tratamento de apóstrofos
- Validação de entradas numéricas

## Estrutura atual

O projeto utiliza módulos separados para organizar responsabilidades:

- `banco_main.py` — fluxo principal do sistema e menu inicial
- `opcoes_menu.py` — tratamento das opções e operações do menu
- `adicionar_clientes.py` — operações relacionadas aos dados dos clientes
- `clientes.py` — classes relacionadas aos clientes e suas movimentações
- `validar_entradas.py` — classe responsável pelas validações de nomes e números
- `valida_entrada.py` — módulo de validação anterior, em processo de substituição

Os dados dos clientes são armazenados localmente em `local_clientes/dados_clientes.json` e não são versionados pelo Git.

## Conceitos praticados

Durante o desenvolvimento estou praticando conceitos como:

- Variáveis e tipos de dados
- Condicionais e laços de repetição
- Funções e retorno de valores
- Listas e dicionários
- Manipulação de strings
- Manipulação de arquivos JSON
- Módulos e organização de código
- Tratamento de erros e validação de entradas
- Classes e objetos
- Construtores com `__init__`
- Atributos e métodos de instância
- Utilização de `self`
- Referências entre objetos
- Alteração do estado de objetos
- Integração gradual de POO ao código existente
- Git e GitHub
- Branches e Pull Requests
- Integração Contínua com GitHub Actions

## Desenvolvimento

O projeto está em desenvolvimento e passa por uma refatoração gradual da estrutura procedural para Programação Orientada a Objetos.

As classes estão sendo introduzidas conforme novas responsabilidades são identificadas, sem reescrever todo o sistema de uma única vez.

Atualmente, a classe `Validar_entradas` já implementa validações de nomes e entradas numéricas, sendo utilizada em diferentes partes do sistema.

### Próximas etapas

- Implementar `validar_monetario()` para valores de depósitos e saques
- Concluir a substituição do módulo antigo `valida_entrada.py`
- Continuar a integração de POO às operações bancárias
- Ampliar os testes e melhorar o tratamento de entradas inválidas

## Status

**Em desenvolvimento — refatoração gradual para POO.**

**Don't give up; you have a bright future. — by Anonymous**