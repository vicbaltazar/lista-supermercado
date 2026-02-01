import json
from pathlib import Path

ARQUIVO = Path("lista.json")

def carregar_produtos():
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)
    
def montar_lista_supermercado(produtos, rating_minimo):
    produtos_filtrados = [p for p in produtos if p.get("rating", 0) >= rating_minimo]

    lista = {
        "Café da Manhã": [],
        "Frutas e sobremesas": [],
        "Refeições salgadas": [],
        "Bebidas": [],
        "Pet": []
    }

    for p in produtos_filtrados:
        tipo = p.get("type")
        item = {
            "name": p.get("title"),
            "price": p.get("price"),
            "rating": p.get("rating"),
            "type": tipo
        }

        if tipo in ["dairy", "bakery"]:
            lista["Café da Manhã"].append(item)
        if tipo == "fruit":
            lista["Frutas e sobremesas"].append(item)
        if tipo in ["vegetable", "meat", "bakery"]:
            lista["Refeições salgadas"].append(item)
        
        titulo = (p.get("title") or "").lower()
        if any(palavra in titulo for palavra in ["suco", "smoothie"]):
            lista["Bebidas"].append(item)
        
        if tipo == "pet":
            lista["Pet"].append(item)

    return lista

def mostrar_lista(lista):
    total_geral = 0.0
    for categoria, itens in lista.items():
        print(f"\n--- {categoria} ---")
        if not itens:
            print("Nenhum item nesta categoria.")
            continue

        total_categoria = 0.0
        for item in itens:
            nome = item["name"]
            preco = item["price"]
            rating = item["rating"]
            tipo = item["type"]
            total_categoria += preco
            print(f"- {nome} ({tipo}) | Preço: R$ {preco:.2f} | Rating: {rating}")

        total_geral += total_categoria
        print(f"Total da categoria '{categoria}': R$ {total_categoria:.2f}")

    print(f"\n=== TOTAL GERAL DA COMPRA: R$ {total_geral:.2f} ===")

def main():
    if not ARQUIVO.exists():
        print(f"Arquivo {ARQUIVO} não encontrado.")
        return

    produtos = carregar_produtos()
    lista = montar_lista_supermercado(produtos, rating_minimo=3.5)
    mostrar_lista(lista)

if __name__ == "__main__":
    main()
