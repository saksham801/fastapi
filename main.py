from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Success"}

# This is the ONLY way Cloudflare knows how to talk to FastAPI
async def on_fetch(request, env):
    return await app(request, env)