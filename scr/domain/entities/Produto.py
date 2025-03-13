from pydantic import BaseModel

class Produto(BaseModel):
    id_produto: int = None
    descricao: str = None
    foto: str = None
    valor_unitario: str = None