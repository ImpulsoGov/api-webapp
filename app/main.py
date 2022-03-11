from fastapi import FastAPI
from routers import hello,suporte
app = FastAPI()

app.include_router(hello.router)
app.include_router(suporte.router)

@app.get("/")
async def main():
    return {"message":"Olha uma nova API esta rodando :)"}
