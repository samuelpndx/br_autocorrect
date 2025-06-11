# br_autocorrect - Corretor Ortográfico Simples ✍️

`br_autocorrect` é um projeto simples de corretor ortográfico para o Português Brasileiro. Ele permite que o usuário insira uma palavra e verifica se ela existe em um dicionário. Caso a palavra não seja encontrada, o sistema sugere palavras semelhantes com base na distância de Levenshtein.

Acesse a demonstração ao vivo do sistema no seguinte link: [Live Preview](https://br-autocorrect.vercel.app/)


## ✨ Funcionalidades

*   Verificação ortográfica de palavras em Português Brasileiro.
*   Sugestão de palavras corretas para termos digitados incorretamente.
*   Interface web simples e intuitiva construída com Flask.
*   Utiliza a distância de Levenshtein para encontrar sugestões.

## 🛠️ Tecnologias Utilizadas

*   **Python**: Linguagem de programação principal.
*   **Flask**: Microframework web para a interface do usuário.
*   **Levenshtein Distance**: Algoritmo para calcular a similaridade entre strings.

## 🚀 Configuração e Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/samuelpndx/br_autocorrect.git
    cd br_autocorrect
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    # No Windows
    # venv\Scripts\activate
    # No macOS/Linux
    # source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação Flask:**
    ```bash
    flask run
    ```
    Acesse a aplicação no seu navegador, geralmente em `http://127.0.0.1:5000/`.

## 📖 Como Usar

1.  Abra o navegador e acesse o endereço da aplicação (ex: `http://127.0.0.1:5000/`).
2.  Digite a palavra que deseja verificar no campo de texto.
3.  Clique no botão "Verificar".
4.  O sistema informará se a palavra está correta, ou sugerirá alternativas caso esteja incorreta e sugestões sejam encontradas.

## 🧠 Como Funciona (Resumo)

*   **Carregamento do Vocabulário**: Ao iniciar, a aplicação carrega uma lista de palavras de um arquivo de dicionário.
*   **Verificação**: Quando uma palavra é submetida:
    *   Ela é convertida para minúsculas.
    *   O sistema verifica se a palavra existe no vocabulário carregado.
*   **Sugestões**: Se a palavra não for encontrada:
    *   O algoritmo de **Distância de Levenshtein** é usado para calcular a "distância de edição" entre a palavra inserida e cada palavra do vocabulário.
    *   As palavras do vocabulário com as menores distâncias (ou seja, mais similares) são apresentadas como sugestões.
