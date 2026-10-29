import collections
import collections.abc

# Correção para compatibilidade do módulo experta com Python 3.10+
collections.Mapping = collections.abc.Mapping

from experta import *

class RespostasUsuario(Fact):
    pass

class ConsultorCarreiraTI(KnowledgeEngine):
    
    @DefFacts()
    def _initial_action(self):
        yield RespostasUsuario(acao="avaliar")

    # 1. Back-end
    @Rule(RespostasUsuario(matematica='Média', atuacao='Escrever algoritmos lógicos e criar APIs', ferramenta='Java, C# ou Python'))
    def regra_backend(self):
        self.declare(Fact(trilha="Desenvolvimento Back-end", justificativa="O seu perfil foca na lógica de servidores, regras de negócio e manipulação de bases de dados."))

    # 2. Front-end & UI/UX
    @Rule(RespostasUsuario(matematica='Baixa', atuacao='Criar layouts visuais e interfaces responsivas', ferramenta='JavaScript (React, Angular, Vue)'))
    def regra_frontend(self):
        self.declare(Fact(trilha="Desenvolvimento Front-end & UI/UX", justificativa="O seu foco em design e experiência do utilizador direciona-o para o Front-end."))

    # 3. Ciência de Dados
    @Rule(RespostasUsuario(matematica='Alta', atuacao='Analisar grandes massas de dados e modelagem', ferramenta='Python (Pandas, Scikit-learn) ou R'))
    def regra_ciencia_dados(self):
        self.declare(Fact(trilha="Ciência de Dados e Machine Learning", justificativa="A sua alta afinidade matemática e perfil analítico são essenciais para modelagem preditiva e IA."))

    # 4. Engenharia de Dados
    @Rule(RespostasUsuario(matematica='Alta', atuacao='Construir pipelines (ETL/ELT) e arquitetura', ferramenta='SQL, Spark ou Python'))
    def regra_engenharia_dados(self):
        self.declare(Fact(trilha="Engenharia de Dados", justificativa="Tem o perfil ideal para criar infraestruturas robustas que sustentam a análise de dados."))

    # 5. Cibersegurança
    @Rule(RespostasUsuario(matematica='Média', atuacao='Analisar vulnerabilidades e defesa cibernética', ferramenta='Linux, Redes ou ferramentas de Pentest'))
    def regra_ciberseguranca(self):
        self.declare(Fact(trilha="Cibersegurança (Security / Pentesting)", justificativa="O seu interesse em redes e defesa direciona-o para a proteção de sistemas contra ameaças."))

    # 6. DevOps & SRE
    @Rule(RespostasUsuario(matematica='Média', atuacao='Automatizar processos de CI/CD e contêineres', ferramenta='Docker, Kubernetes ou Linux'))
    def regra_devops(self):
        self.declare(Fact(trilha="DevOps & SRE", justificativa="O seu foco em automação e infraestrutura ágil é o núcleo da cultura DevOps."))

    # 7. Cloud Architecture
    @Rule(RespostasUsuario(matematica='Média', atuacao='Planejar e migrar infraestruturas escaláveis', ferramenta='AWS, Azure ou GCP'))
    def regra_cloud(self):
        self.declare(Fact(trilha="Computação em Nuvem (Cloud Architecture)", justificativa="Ideal para planear arquiteturas distribuídas e de alta disponibilidade na nuvem."))

    # 8. Mobile
    @Rule(RespostasUsuario(matematica='Baixa', atuacao='Desenvolver para ecossistemas de smartphones', ferramenta='Flutter, React Native, Swift ou Kotlin'))
    def regra_mobile(self):
        self.declare(Fact(trilha="Desenvolvimento Mobile", justificativa="O seu perfil encaixa na criação de aplicações otimizadas para dispositivos móveis."))

    # 9. QA (Qualidade)
    @Rule(RespostasUsuario(matematica='Baixa', atuacao='Criar testes automatizados e revisar processos', ferramenta='Selenium, Cypress ou JUnit'))
    def regra_qa(self):
        self.declare(Fact(trilha="Engenharia de Qualidade e Testes (QA)", justificativa="Foco metódico em garantir que o software seja entregue sem falhas."))

    # 10. Product Management
    @Rule(RespostasUsuario(matematica='Baixa', atuacao='Fazer a ponte entre negócio e desenvolvimento', ferramenta='Nenhuma / Jira e Metodologias Ágeis'))
    def regra_pm(self):
        self.declare(Fact(trilha="Gestão de Produtos (Product Management)", justificativa="O seu perfil foca no valor final, alinhando objetivos de negócio com as equipas técnicas."))

    def obter_resultado(self):
        trilha = None
        justificativa = None
        for fact in self.facts.values():
            if 'trilha' in fact:
                trilha = fact['trilha']
            if 'justificativa' in fact:
                justificativa = fact['justificativa']
        return trilha, justificativa