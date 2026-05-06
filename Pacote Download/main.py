from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Configuração do banco de dados
engine = create_engine("sqlite:///etiquetas.db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Tabela no banco
class EtiquetaDB(Base):
    __tablename__ = "etiquetas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    largura = Column(Float)
    altura = Column(Float)

Base.metadata.create_all(bind=engine)

# Modelo de entrada
class Etiqueta(BaseModel):
    nome: str
    largura: float
    altura: float

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def inicio():
    return {"mensagem": "API de etiquetas funcionando!"}

@app.get("/etiquetas")
def listar_etiquetas(db: Session = Depends(get_db)):
    return db.query(EtiquetaDB).all()

@app.post("/etiquetas")
def cadastrar_etiqueta(etiqueta: Etiqueta, db: Session = Depends(get_db)):
    nova = EtiquetaDB(**etiqueta.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return {"mensagem": "Etiqueta cadastrada!", "dados": nova}

@app.put("/etiquetas/{id}")
def atualizar_etiqueta(id: int, etiqueta: Etiqueta, db: Session = Depends(get_db)):
    registro = db.query(EtiquetaDB).filter(EtiquetaDB.id == id).first()
    if not registro:
        return {"erro": "Etiqueta não encontrada"}
    registro.nome = etiqueta.nome
    registro.largura = etiqueta.largura
    registro.altura = etiqueta.altura
    db.commit()
    db.refresh(registro)
    return {"mensagem": "Etiqueta atualizada!", "dados": registro}

@app.delete("/etiquetas/{id}")
def deletar_etiqueta(id: int, db: Session = Depends(get_db)):
    registro = db.query(EtiquetaDB).filter(EtiquetaDB.id == id).first()
    if not registro:
        return {"erro": "Etiqueta não encontrada"}
    db.delete(registro)
    db.commit()
    return {"mensagem": "Etiqueta deletada!"}