# 🔴 iFood SmartAgent - Engenharia de IA Aplicada à Retenção de Parceiros

O **iFood SmartAgent** é uma solução funcional de Inteligência Artificial desenvolvida para resolver uma dor crítica de negócio no ecossistema de marketplace do iFood: a gestão ágil e humanizada de feedbacks críticos enviados por clientes aos restaurantes parceiros. 

A aplicação automatiza o processo de suporte técnico e triagem de dados, transformando avaliações textuais não estruturadas em relatórios analíticos estruturados em tempo real.

---

## 🛠️ Arquitetura Técnica e Boas Práticas

Para demonstrar maturidade arquitetural e simular o cenário de um microsserviço de produção, o projeto foi dividido estritamente em camadas:

*   **Orquestração de IA (Back-end):** Desenvolvido em Python utilizando o framework **LangChain**. A lógica foi construída utilizando a sintaxe contemporânea **LCEL (LangChain Expression Language)** através do operador de cadeias (`|`), interligando um `ChatPromptTemplate`, o motor de inferência local e um `StrOutputParser`.
*   **Inferência Local (Ollama):** Visando custo zero de infraestrutura e total privacidade de dados (em conformidade com preceitos de cibersegurança defensiva), a aplicação utiliza o modelo open-source **Qwen 8B** rodando localmente via **Ollama**.
*   **Segurança de Credenciais:** Implementação de isolamento de infraestrutura utilizando variáveis de ambiente via arquivo oculto `.env`, blindando a URL do servidor local de inferência.
*   **Camada Visual (Front-end):** Interface amigável e interativa projetada via **Streamlit**, simulando o portal operacional real utilizado por um tomador de decisão ou dono de restaurante parceiro.

---

## 📊 Demonstração do Fluxo de Dados (Exemplo Prático)

Para fins de validação do comportamento do agente sem a necessidade de execução local, este é o padrão de processamento esperado pelo pipeline:

**Entrada Textual do Usuário (Painel do Restaurante):**
> *"Minha janta demorou quase uma hora além do prazo. O entregador deixou a sacola cair no portão, o que fez com que o refrigerante explodisse e molhasse todo o lanche que acabou vindo frio. Quero meu dinheiro de volta."*

**Saída Estruturada Gerada pela LLM (Mapeamento JSON):**
```json
{
  "classificacao": "Logística/Atraso",
  "gravidade": "Alta",
  "resposta_cliente": "Olá! Lamentamos profundamente pelo atraso de quase uma hora e pelo ocorrido com a entrega do seu pedido. Essa experiência não reflete o nosso padrão de qualidade. Já estamos entrando em contato com a equipe de logística do iFood para averiguar a conduta do entregador. Em paralelo, realizamos o estorno integral do valor pago pelo seu lanche e refrigerante. Esperamos ter uma nova oportunidade de te atender muito melhor em breve!"
}
```

---

## 🚀 Como Executar o Projeto na sua Máquina

Siga o passo a passo abaixo no terminal do seu editor de código (VS Code) para preparar o ambiente e rodar a aplicação:

### 1. Pré-requisitos
Certifique-se de ter o **Ollama** instalado na sua máquina. O projeto foi estruturado utilizando o modelo `qwen3:8b`.

```bash
# Baixar o modelo padrão do projeto
ollama run qwen3:8b
```

💡 **Nota sobre Versões e Modelos:** Caso você prefira utilizar outro modelo (como `llama3.2` ou `gemma2`), ou possua uma versão diferente instalada, basta:
1. Validar os modelos disponíveis na sua máquina rodando: `ollama list`
2. Abrir o arquivo `brain.py` e alterar o parâmetro `model="NOME_DO_SEU_MODELO"` na inicialização do `ChatOllama` (Linha 34).


### 2. Clonar o Repositório e Acessar a Pasta
```bash
git clone https://github.com
cd ifood_smartagent
```

### 3. Criar e Ativar o Ambiente Virtual (venv)
Execute a criação do ambiente no seu terminal:
```bash
python -m venv venv
```

Agora, **escolha APENAS UM** dos comandos abaixo para ativar, dependendo do terminal que você está utilizando no seu VS Code:

*   **Opção A: Se o seu terminal for o PowerShell (Padrão do VS Code - Exibe `PS` no início da linha):**
    *   *Caso o Windows bloqueie scripts por diretivas de segurança, execute este comando de liberação primeiro:*
        ```powershell
        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
        ```
    *   *Em seguida, ative o ambiente:*
        ```powershells
        & .\venv\Scripts\Activate.ps1
        ```

*   **Opção B: Se o seu terminal for o Prompt de Comando (CMD tradicional):**
    ```bash
    .\venv\Scripts\activate.bat
    ```

*   **Opção C: Se você estiver utilizando Linux ou macOS:**
    ```bash
    source venv/bin/activate
    ```

*(A ativação terá funcionado quando o prefixo `(venv)` aparecer no início da linha do seu terminal).*


### 4. Instalar as Dependências
```bash
pip install langchain langchain-core langchain-ollama streamlit python-dotenv
```

### 5. Configurar as Variáveis de Ambiente
Crie um arquivo chamado **`.env`** na raiz do projeto e adicione a URL do seu servidor Ollama local (esta configuração será ignorada pelo Git conforme regras do `.gitignore`):
```text
OLLAMA_BASE_URL=http://localhost:11434
```

### 6. Executar a Aplicação
Com o ambiente ativamente preparado e o Ollama rodando em segundo plano, execute o comando:
```bash
streamlit run app.py
```
A interface gráfica abrirá automaticamente no seu navegador no endereço `http://localhost:8501`.
