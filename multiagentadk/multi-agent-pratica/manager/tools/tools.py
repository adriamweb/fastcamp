# Estoque simples em memória: dicionário com nome do produto -> {preço, quantidade}
STOCK = {
    "camiseta": {"price": 49.90, "quantity": 10},
    "calca":    {"price": 89.90, "quantity": 5},
    "tenis":    {"price": 199.90, "quantity": 3},
    "bone":     {"price": 39.90, "quantity": 8},
}


def list_products() -> dict:
    """Lista todos os produtos disponíveis com preço e quantidade."""
    available = {
        name: info
        for name, info in STOCK.items()
        if info["quantity"] > 0
    }
    return {"status": "success", "products": available}


def sell_product(product: str, quantity: int) -> dict:
    """Realiza a venda de um produto, decrementando o estoque."""
    product = product.lower()

    if product not in STOCK:
        return {"status": "error", "message": f"Produto '{product}' não encontrado."}

    item = STOCK[product]

    if item["quantity"] < quantity:
        return {
            "status": "error",
            "message": f"Estoque insuficiente. Disponível: {item['quantity']} unidade(s).",
        }

    # Decrementa o estoque e calcula o total da venda
    item["quantity"] -= quantity
    total = item["price"] * quantity

    return {
        "status": "success",
        "product": product,
        "quantity_sold": quantity,
        "unit_price": item["price"],
        "total": total,
        "remaining_stock": item["quantity"],
    }


def check_stock(product: str) -> dict:
    """Verifica a quantidade disponível de um produto específico."""
    product = product.lower()

    if product not in STOCK:
        return {"status": "error", "message": f"Produto '{product}' não encontrado."}

    item = STOCK[product]
    return {
        "status": "success",
        "product": product,
        "quantity": item["quantity"],
        "price": item["price"],
    }
