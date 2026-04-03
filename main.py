from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "HEllo Claude"}

@app.get("/login")
async def login():
    return {"message": "Hello login"}

# This is the ONLY way Cloudflare knows how to talk to FastAPI
async def on_fetch(request, env):
    return await app(request, env)

#hello