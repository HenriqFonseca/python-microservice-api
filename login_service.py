from fastapi import FastAPI,HTTPException
from typing import List
from pydantic import BaseModel
import json
app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    password: str




@app.post("/login")
async def login(user:User):
    if user.username == "user" and user.password == "password":
        return {"status": "sucesso", "mensagem": "Usuário autenticado"}
    else:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

