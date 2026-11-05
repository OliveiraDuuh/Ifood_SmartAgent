import os
from dotenv import load_dotenv  # Biblioteca que lê as configurações escondidas do .env
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

# Carrega as variáveis do arquivo .env para a memória da aplicação
load_dotenv()

def inicializar_agente():
    """
    Monta a cadeia estruturada do LangChain buscando a configuração do .env
    """
    # 1. Definição do Prompt (O comportamento do seu Agente de IA especialista no iFood)
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", (
            "Você é o iFood SmartAgent, uma IA especialista em suporte e retenção de clientes para restaurantes parceiros. "
            "Sua tarefa é analisar a reclamação que o restaurante recebeu e gerar um JSON estrito contendo os campos: "
            "'classificacao' (Logística/Atraso, Qualidade da Comida ou Erro no Pedido), "
            "'gravidade' (Baixa, Média ou Alta) e "
            "'resposta_cliente' (Uma resposta empática, profissional, em português, oferecendo uma solução inteligente em nome do restaurante)."
        )),
        ("user", "Analise a seguinte avaliação crítica: {avaliacao}")
    ])
    
    # Puxa o endereço do Ollama que guardamos com segurança no .env
    endereco_ollama = os.getenv("OLLAMA_BASE_URL")
    
    # 2. Inicialização do Modelo Local apontando para o seu modelo atual qwen3:8b
    modelo = ChatOllama(
        base_url=endereco_ollama,
        model="qwen3:8b", 
        temperature=0.3
    )
    
    # 3. Conversor de Saída (Garante que a resposta venha como string limpa)
    parser = StrOutputParser()
    
    # 4. Construção da Chain (Conectando tudo com o operador '|' que você viu no vídeo)
    cadeia_ia = prompt_template | modelo | parser
    
    return cadeia_ia
