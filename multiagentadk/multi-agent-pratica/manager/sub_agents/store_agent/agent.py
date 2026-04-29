from google.adk.agents import Agent

# Importa as ferramentas de estoque e venda
from ...tools.tools import check_stock, list_products, sell_product

# Sub-agente para fazer as vendas: consulta produtos, verifica o estoque e realiza as vendas.
store_agent = Agent(
    name="store_agent",
    model="gemini-2.0-flash",
    description="Agente de vendas da loja. Consulta produtos, estoque e realiza vendas.",
    instruction="""
    Você é o vendedor da UFGStore, uma loja de roupas.

    Você tem acesso às seguintes ferramentas:
    - list_products: lista todos os produtos disponíveis com preço e quantidade
    - check_stock: verifica o estoque de um produto específico
    - sell_product: realiza a venda de um produto

    Quando o cliente quiser comprar, confirme o produto e a quantidade antes de chamar sell_product.
    Sempre informe o total da compra e o estoque restante após a venda.
    Se um produto estiver sem estoque, informe o cliente educadamente.
    """,
    tools=[list_products, check_stock, sell_product],
)
