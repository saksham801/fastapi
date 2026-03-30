from fastapi import FastAPI
import sys

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Hello from Cloudflare Workers!",
        "python_version": sys.version,
        "fastapi_status": "loaded"
    }

@app.get("/test")
async def test():
    return {"status": "success"}