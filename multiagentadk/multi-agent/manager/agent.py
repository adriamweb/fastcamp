# comentário feito por mim: importa a classe Agent para criar os agentes.
from google.adk.agents import Agent

# comentário feito por mim: importa AgentTool para que seja possível usar um agente
# como uma ferramenta, como é no caso do news_analyst
from google.adk.tools.agent_tool import AgentTool

# comentário feito por mim: importa todos os subagentes que foram criados, onde funny_nerd e stock_analyst
# serão usados como subagentes, e news_analyst será usado como AgentTool do manager. 
from .sub_agents.funny_nerd.agent import funny_nerd
from .sub_agents.news_analyst.agent import news_analyst
from .sub_agents.stock_analyst.agent import stock_analyst

# importa a ferramenta que traz a data e hora formatada.
from .tools.tools import get_current_time

# comentário feito por mim: definição do agente manager (precisa ser chamado de root_agent).
# o agente atua como um orquestrador, recebendo de fato a mensagem do usuário e decidindo como
# a formulação da resposta iŕa acontecer, podendo delegar aos sub-agentes e usar tools para responder.


root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="Manager agent",
    instruction="""
    You are a manager agent that is responsible for overseeing the work of the other agents.

    Always delegate the task to the appropriate agent. Use your best judgement 
    to determine which agent to delegate to.

    You are responsible for delegating tasks to the following agent:
    - stock_analyst
    - funny_nerd

    You also have access to the following tools:
    - news_analyst
    - get_current_time
    """,
    # comentário feito por mim: caso o agente delegue a tarefa para um sub-agente, ele irá
    # tomar as rédeas da conversa por inteiro, respondendo e posteriormente o controle voltaŕa para o manager. 
    sub_agents=[stock_analyst, funny_nerd],

    # comentário feito por mim: as ferramentas são usadas para retornar valores, então no caso do news_analyst, 
    # o manager irá requisitar as informações de uma determinada notícia e o agenttool irá apenas responder
    # a pergunta, mas sem tomar as rédeas da conversa. 
    tools=[
        AgentTool(news_analyst),
        get_current_time,
    ],
)
