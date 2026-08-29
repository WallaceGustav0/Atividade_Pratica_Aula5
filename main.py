from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="API de Chamados")

class ChamadoEntrada(BaseModel):
    titulo: str
    descricao: str
    prioridade: str

chamados = []

# Implementação da rota inicial e a listagem
@app.get("/")
def inicio():
    return {"mensagem": "API de Chamados ativa"}

@app.get("/chamados")
def listar_chamados():
    return chamados


# Implementação da criação
@app.post("/chamados", status_code=status.HTTP_201_CREATED)
def criar_chamado(dados: ChamadoEntrada):
    chamado = {
        "id": len(chamados) + 1,
        **dados.model_dump(),
        "status": "aberto"
    }
    chamados.append(chamado)
    return chamado


# Implementação d
# a consulta por id
@app.get("/chamados/{chamado_id}")
def buscar_chamado(chamado_id: int):
    for chamado in chamados:
        if chamado["id"] == chamado_id:
            return chamado
    raise HTTPException(
        status_code=404,
        detail="Chamado não encontrado"
    )


# Desafio adicional:
# Busca chamados pelo status
@app.get("/chamados/status/{status_chamado}")
def buscar_chamados_por_status(status_chamado: str):
    resultado = []

    for chamado in chamados:
        if chamado["status"] == status_chamado:
            resultado.append(chamado)

    return resultado