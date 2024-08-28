from fastapi.responses import RedirectResponse
from fastapi import FastAPI
from app import cves
import uvicorn

app = FastAPI()
app.include_router(cves.router)


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

if __name__ == '__main__':
    uvicorn.run('app.main:app', host='127.0.0.1', port=8000, reload=True)
