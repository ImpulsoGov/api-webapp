from fastapi import Request, Response

QUANTIDADE_SEGUNDOS_24_HORAS = 60 * 60 * 24

async def adiciona_cache_header(request: Request, response: Response):
    response.headers["Cache-Control"] = f"private, max-age={QUANTIDADE_SEGUNDOS_24_HORAS}"
    return response