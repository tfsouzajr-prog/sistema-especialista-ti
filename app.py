import streamlit as st
from motor import ConsultorCarreiraTI, RespostasUsuario

st.title("Consultor Inteligente de Carreiras em TI")
st.write("Responda às perguntas abaixo para descobrir a sua trilha ideal.")

opcoes_atuacao = [
    "Escrever algoritmos lógicos e criar APIs",
    "Criar layouts visuais e interfaces responsivas",
    "Analisar grandes massas de dados e modelagem",
    "Construir pipelines (ETL/ELT) e arquitetura",
    "Analisar vulnerabilidades e defesa cibernética",
    "Automatizar processos de CI/CD e contêineres",
    "Planejar e migrar infraestruturas escaláveis",
    "Desenvolver para ecossistemas de smartphones",
    "Criar testes automatizados e revisar processos",
    "Fazer a ponte entre negócio e desenvolvimento"
]

opcoes_ferramentas = [
    "Java, C# ou Python",
    "JavaScript (React, Angular, Vue)",
    "Python (Pandas, Scikit-learn) ou R",
    "SQL, Spark ou Python",
    "Linux, Redes ou ferramentas de Pentest",
    "Docker, Kubernetes ou Linux",
    "AWS, Azure ou GCP",
    "Flutter, React Native, Swift ou Kotlin",
    "Selenium, Cypress ou JUnit",
    "Nenhuma / Jira e Metodologias Ágeis"
]

matematica = st.selectbox("1. Qual a sua afinidade com Matemática e Estatística?", ["Baixa", "Média", "Alta"])
atuacao = st.selectbox("2. O que prefere fazer no dia a dia?", opcoes_atuacao)
ferramenta = st.selectbox("3. Qual a sua ferramenta/linguagem de maior afinidade?", opcoes_ferramentas)

if st.button("Diagnosticar Carreira"):
    engine = ConsultorCarreiraTI()
    engine.reset()
    engine.declare(RespostasUsuario(matematica=matematica, atuacao=atuacao, ferramenta=ferramenta))
    engine.run()
    
    trilha, justificativa = engine.obter_resultado()
    
    if trilha:
        st.success(f"**Trilha Recomendada:** {trilha}")
        st.info(f"**Justificativa:** {justificativa}")
    else:
        st.warning("Não foi possível determinar uma trilha exata com essa combinação de respostas específicas. Tente ajustar o seu perfil.")