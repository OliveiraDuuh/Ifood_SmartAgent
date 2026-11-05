import streamlit as tf
import json
from brain import inicializar_agente

# Configuração visual da página (Estilo e cores do iFood)
tf.set_page_config(page_title="iFood SmartAgent", page_icon="🔴", layout="centered")

# Estilização básica e título principal da tela
tf.title("🔴 iFood SmartAgent")
tf.subheader("Portal de Inteligência Artificial para Restaurantes Parceiros")
tf.caption("Analise feedbacks críticos de clientes e gere respostas de suporte instantâneas utilizando IA.")

# Caixa de entrada de texto grande para o usuário colar a avaliação do app
avaliacao_usuario = tf.text_area(
    label="Cole aqui a avaliação negativa recebida no aplicativo:",
    placeholder="Ex: Minha pizza demorou 1 hora para chegar, veio totalmente fria e o refrigerante não foi entregue.",
    height=120
)

# Botão de disparo que inicia o processamento do Agente de IA
if tf.button("Analisar Feedback com IA"):
    if avaliacao_usuario.strip() == "":
        tf.warning("Por favor, insira o texto de uma avaliação antes de continuar.")
    else:
        with tf.spinner("O Agente do iFood está processando a melhor tratativa..."):
            try:
                # Inicializa a Chain do LangChain importada do arquivo brain.py
                agente = inicializar_agente()
                
                # Invoca a cadeia enviando o texto digitado pelo usuário na variável dinâmica
                resposta_pura = agente.invoke({"avaliacao": avaliacao_usuario})
                
                # Remove possíveis formatações markdown automáticas que a LLM possa gerar (ex: ```json)
                resposta_limpa = resposta_pura.replace("```json", "").replace("```", "").strip()
                
                # Converte a string JSON estruturada em um dicionário utilizável do Python
                dados_resposta = json.loads(resposta_limpa)
                
                tf.success("Análise concluída!")
                
                # Exibindo as métricas e classificações estruturadas na tela em colunas organizadas
                col1, col2 = tf.columns(2)
                with col1:
                    tf.metric(label="Classificação do Problema", value=dados_resposta.get("classificacao"))
                with col2:
                    tf.metric(label="Nível de Gravidade", value=dados_resposta.get("gravidade"))
                
                # Exibindo de forma destacada a sugestão de resposta humanizada gerada pela IA
                tf.write("---")
                tf.markdown("### 📝 Sugestão de Resposta para o Cliente")
                tf.info(dados_resposta.get("resposta_cliente"))
                
                tf.caption("Dica: Você pode copiar o texto acima e utilizá-lo diretamente na aba de avaliações do seu painel iFood.")
                
            except json.JSONDecodeError:
                # Tratamento de erro caso o modelo não retorne um JSON perfeito na CPU
                tf.error("Erro ao estruturar dados automaticamente. Exibindo resposta bruta do modelo:")
                tf.write(resposta_pura)
            except Exception as e:
                tf.error(f"Ocorreu um erro na comunicação com o Ollama: {e}. Certifique-se de que o Ollama está aberto.")
