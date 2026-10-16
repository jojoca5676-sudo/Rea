from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Minha IA de Vídeos")


class PedidoVideo(BaseModel):
    historia: str
    segundos_por_cena: int = 8


@app.get("/")
def inicio():
    return {
        "nome": "Minha IA de Vídeos",
        "status": "Projeto iniciado"
    }


@app.post("/criar-cenas")
def criar_cenas(pedido: PedidoVideo):
    paragrafos = [
        texto.strip()
        for texto in pedido.historia.splitlines()
        if texto.strip()
    ]

    cenas = []

    for numero, texto in enumerate(paragrafos, start=1):
        cenas.append({
            "cena": numero,
            "duracao": pedido.segundos_por_cena,
            "descricao": texto
        })

    return {
        "total_de_cenas": len(cenas),
        "duracao_total": (
            len(cenas) * pedido.segundos_por_cena
        ),
        "cenas": cenas
  }
          
