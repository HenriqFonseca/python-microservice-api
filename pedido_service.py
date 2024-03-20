from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import json

app = FastAPI()


class Pedido(BaseModel):
    pedido_id: int
    user_id: int


def carregarPedido() -> List[Pedido]:
    try:
        with open("./Cache/PedidoCache.txt", "r") as file:
            return [Pedido.parse_raw(line) for line in file]
    except FileNotFoundError:
        return []


def salvarPedido(pedidos: List[Pedido]):
    with open("./Cache/PedidoCache.txt", "w") as file:
        for pedido in pedidos:
            file.write(f"{pedido.json()}\n")


def addPedido(user_id :int,pedido:Pedido) -> Pedido:
    pedido.user_id = user_id
    pedidos = carregarPedido()
    pedidos.append(pedido)
    salvarPedido(pedidos)
    return Pedido





@app.post("/pedido/{user_id}/add")
async def createPedido(user_id: int,pedido:Pedido):
   addPedido(user_id,pedido)
   return {"status": "sucesso", "mensagem": "Pedido criado", "order_id": 123}

