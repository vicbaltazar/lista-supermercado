## 🛒 Lista Supermercado

Aplicação em Python pra gerenciar uma lista de compras com categorias, filtro por rating e cálculo de total — usando um arquivo de produtos em JSON.

## 🚀 Sobre

Esse projeto lê um arquivo produtos.json, filtra os produtos por rating mínimo, organiza por categorias e mostra no terminal o total gasto por categoria e valor total da compra.

## 💡 Funcionalidades

- Filtrar produtos por rating.
- Categorizar itens (ex: Café da Manhã, Bebidas, Pet).
- Mostrar totais por categoria e geral.
- Fácil de estender pra mais filtros ou categorias novas.

## 📦 Como usar

**Clone o repositório**

git clone https://github.com/vicbaltazar/lista-supermercado.git
cd lista-supermercado

Instale dependências (opcional)

Não há dependências externas fora da biblioteca padrão.

Rode o programa

python lista.py
O script vai carregar produtos.json e imprimir a lista organizada com totais.

## 📄 Estrutura do projeto
.
├── produtos.json        # Dados de produtos usados como base
├── lista.py             # Script principal
└── README.md            # Este arquivo

## 🧠 Como funciona
O programa:

Lê os produtos de produtos.json.

Filtra por rating mínimo.

Agrupa por categorias como "Café da Manhã", "Bebidas", "Pet", etc.

Mostra no terminal com totais por grupo e geral.
