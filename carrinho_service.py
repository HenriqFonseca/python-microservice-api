from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import json

app = FastAPI()


class Carrinho(BaseModel):
    user_id: int
    produto_id: int
    quantidade: int

def carregarCarrinho() -> List[Carrinho]:
    try:
        with open("./Cache/CarrinhoCache.txt", "r") as file:
            return [Carrinho.parse_raw(line) for line in file]
    except FileNotFoundError:
        return []



def salvarCarrinho(carrinhos: List[Carrinho]):
    with open("./Cache/CarrinhoCache.txt", "w") as file:
        for carrinho in carrinhos:
            file.write(f"{carrinho.json()}\n")


def addCarrinho(carrinho:Carrinho,user_id) -> Carrinho:
    carrinho.user_id = user_id
    carrinho.produto_id = carrinho.produto_id
    carrinho.quantidade = carrinho.quantidade
    carrinhos = carregarCarrinho()
    carrinhos.append(carrinho)
    salvarCarrinho(carrinhos)
    return carrinho


@app.post("/carrinho/{user_id}/add")
async def createCarrinho(carrinho:Carrinho,user_id):
    return addCarrinho(carrinho,user_id)


@app.get("/carrinho/{user_id}/")
async def getCarrinho(carrinho:Carrinho, user_id_param):
    if carrinho.user_id == user_id_param:
        with open("./Cache/CarrinhoCache.txt", "r") as file:
            return [Carrinho.parse_raw(line) for line in file]
    return "Carrinho não encontrado"