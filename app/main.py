from fastapi import FastAPI
from routers import hello,suporte,impulso_previne
app = FastAPI()

app.include_router(hello.router)
app.include_router(suporte.router)
app.include_router(impulso_previne.router)

@app.get("/")
async def main():
    return {"message":"Olha uma nova API esta rodando :)"}
