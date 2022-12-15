# User jobs

Projeto de análise a partir de um conjunto de dados sobre empregos atravez de leitura e manipulação de arquivo .csv com a linguagem de programação python.
O projeto consiste em uma página Web que disponibiliza informações de vagas de empregos e suas características. 


**Obs**: O lyout da aplicação front-end é de autoria da trybe.


## Executado o projeto

Para executar o projeto primeiro você deve fazer o clone deste repositório, após isto deve abrir o projeto em algum editor de códigos.

**OBS**: Para que este projeto seja execultado você obritóriamente deve ter o ```python``` instalado em sua máquina, caso não tenha execulte o comando abixo para fazer a instalação em ambientes linux.

```
    sudo apt install python3
```

Verificando se o python foi instalado

```
    python3 --version
```

A saída deverá:

```
    Python 3.8.0
```

Criar o ambiente virtual:

```
    python3 -m venv .venv
```

Ativar o ambiente virtual
```
    source .venv/bin/activate
```

Instalar as dependências no ambiente virtual

```
    python3 -m pip install -r dev-requirements.txt
```

Agora sua aplicação esta configurada e já pode ser execultada com o comando abaixo.

```
    flask run
```

**OBS**: Após rodar o comando acima no próprio terminal será disponibilizado um endereço como no exemplo abixo:

```
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

**OBS**: Agora você deve clicar em ```Jobs```que se encontra no menu na parte superior da tela, logo será exibido as informações de emprengos disponiveís.
## Habilidades trabalhadas:

- Uso do terminal interativo do Python.
- Utilização de estruturas condicionais e de repetição.
- Utilização funções built-in do Python.
- Tratamento de exceções em Python.
- Manipulação de arquivos em .csv.
- Escrita de teste com Pytest.
- Utilização de módulos proprios e importação em outros códigos.

## Tecnologias 

- **Python** - Linguagem de programação
- **Pytest** - Ferramenta de teste Python
- **Flack8** - Linter de códigos python
- **Black** - Formatador de código Python


## Rodando os testes

Para rodar os testes, rode o seguinte comando

```bash
  pytest
```