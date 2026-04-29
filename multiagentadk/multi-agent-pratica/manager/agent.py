from google.adk.agents import Agent

# Importa os dois sub-agentes criados
from .sub_agents.receptionist.agent import receptionist
from .sub_agents.store_agent.agent import store_agent

# root_agent é o orquestrador: recebe a mensagem do usuário e decide
# para qual sub-agente delegar. Quando delega, o sub-agente assume a conversa por inteiro.
root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="Manager da loja. Orquestra a recepção e as vendas.",
    instruction="""
    Você é o gerente da FastStore.

    Delegue as tarefas da seguinte forma:
    - Se o cliente está chegando, se apresentando ou cumprimentando: delegue ao receptionist
    - Se o cliente quer ver produtos, verificar estoque ou comprar algo: delegue ao store_agent

    Não responda diretamente — sempre delegue ao agente correto.
    """,
    # informa ao root_agente quais são os seus sub-agentes.
    sub_agents=[receptionist, store_agent],
)
