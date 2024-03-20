from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import json
app = FastAPI()


class Produto(BaseModel):
    id: int
    nome: str
    preco: int


def carregarProduto() -> List[Produto]:
    try:
        with open("./Cache/ProdutoCache.txt", "r") as file:
            return [Produto.parse_raw(line) for line in file]
    except FileNotFoundError:
        return []


def salvarProduto(produtos: List[Produto]):
    with open("./Cache/ProdutoCache.txt", "w") as file:
        for produto in produtos:
            file.write(f"{produto.json()}\n")


def createProduto(produto:Produto) -> Produto:
    produto.id = produto.id
    produtos = carregarProduto()
    produtos.append(produto)
    salvarProduto(produtos)
    return produto


# Retornar todos os produtos
def getAllProducts() -> List[Produto]:
    return carregarProduto()


@app.get("/produtos")
async def listar_produtos():
    return getAllProducts()


@app.post("/produtos/create")
def adicionarProduto(produto: Produto):
    return createProduto(produto)


