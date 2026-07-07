# 🔍 TING (Trybe is not Google) — Algoritmo de Indexação e Busca de Arquivos

O **TING (Trybe is not Google)** é um programa em Python que simula um sistema simplificado de indexação e busca de documentos, operando de forma análoga aos motores de pesquisa. A aplicação é capaz de importar arquivos de texto brutos (`.txt`), processar seus metadados estruturalmente e realizar varreduras rápidas para identificar a ocorrência de termos específicos.

O foco principal deste projeto foi o estudo prático e a implementação manual de **Estruturas de Dados** lineares, otimizando o gerenciamento de memória e a complexidade de tempo dos algoritmos.

---

## 🚀 Habilidades Desenvolvidas & Consolidadas

Este projeto consolidou conceitos profundos de Estruturas de Dados e algoritmos de busca em Python:

* **Manipulação de Estruturas de Dados Lineares:**
    * Entendimento conceitual e prático de estruturas como **Pilhas**, **Deques**, **Nós**, **Listas Ligadas** e **Listas Duplamente Ligadas**.
* **Implementação de Filas Otimizadas (FIFO):**
    * Desenvolvimento manual da classe `Queue` e seus métodos fundamentais (`enqueue`, `dequeue`, `search`), garantindo complexidade algorítmica adequada para inserção e remoção de elementos.
* **Algoritmos de Priorização com Filas Mutáveis:**
    * Criação de uma estrutura de `PriorityQueue` (Fila de Prioridades) baseada em lógica condicional de tamanho (vagas curtas vs. vagas longas), reordenando dinamicamente a ordem de saída de dados processados.
* **Importação e Parsing de Strings:**
    * Tratamento de fluxos de entrada de dados de arquivos textuais, lidando com formatações de quebras de linha (`\n`), filtragem de extensões inválidas e tratamento de saídas nos canais padrão (`stdout` e `stderr`).
* **Algoritmos de Busca Indexada (Case-Insensitive):**
    * Criação de rotas de pesquisa capazes de mapear a localização exata de termos textuais (retornando o número da linha e o conteúdo textual) em múltiplos arquivos simultaneamente sem alterar a estrutura da fila original.
* **Testes com Pytest voltados a Estruturas Incorretas:**
    * Escrita de testes utilizando asserções de erro (como `IndexError` para posições inválidas na memória) e uso de marcações de falhas esperadas (*XFAIL*).

---

## 📁 Arquitetura dos Módulos Desenvolvidos

A aplicação foi dividida em dois pacotes de responsabilidades distintas:

### 1. Pacote de Gerenciamento (`ting_file_management`)
* **`queue.py`**: Estrutura base de dados que armazena na memória RAM os caminhos e conteúdos dos arquivos textuais processados.
* **`file_management.py`**: Módulo que faz a ponte com o sistema operacional para ler de forma segura os dados do arquivo `.txt`.
* **`file_process.py`**: Transforma os dados brutos lidos em dicionários estruturados, mapeando o nome, quantidade de linhas e metadados estruturais do documento.

### 2. Pacote de Buscas (`ting_word_searches`)
* **`word_search.py`**: Motor de varredura que percorre os elementos indexados na fila para buscar as palavras-chave solicitadas, trazendo informações detalhadas (como o número de linhas e o conteúdo contextualizado de onde o termo aparece).

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **Linguagem Principal:** Python 3 (v3.8+)
* **Framework de Testes:** Pytest
* **Análise Estática de Código:** Flake8 (Conformidade com a PEP 8)
* **Gerenciamento de Escopo:** Ambientes virtuais (`.venv`)

---

## 🏕️ Configuração do Ambiente e Execução

O projeto faz o gerenciamento de suas dependências por meio de ambientes virtuais isolados.

### 1. Preparando o Ambiente Virtual

```bash
# Criar o ambiente virtual
python3 -m venv .venv

# Ativar o ambiente virtual
source .venv/bin/activate

# Instalar as dependências de desenvolvimento
python3 -m pip install -r dev-requirements.txt
```

### 2. Executando os testes automatizados
Com o ambiente virtual ativo, execute o comando abaixo para verificar a integridade das estruturas de dados e funções de busca:

```bash
python3 -m pytest
python3 -m pytest -s -vv
```

### 3. Validação do linter
Para validar a legibilidade e se o projeto segue à risca os padrões de formatação da comunidade Python (PEP 8):
```bash
python3 -m flake8
```

### 4. Exemplo da estrutura de retorno do motor de busca
Ao pesquisar por uma palavra indexada na aplicação, a resposta é consolidada no formato abaixo, especificando os trechos exatos de ocorrência:

```python3
[
    {
        "palavra": "algoritmo",
        "arquivo": "statics/novo_paradigma_globalizado.txt",
        "ocorrencias": [
            {
                "linha": 3,
                "conteudo": "Acima de tudo, entender o algoritmo de indexação..."
            }
        ]
    }
]
```
