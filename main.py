from fastapi import FastAPI, Request
from web import explorer,creature,user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(explorer.router)
app.include_router(creature.router)
app.include_router(user)


#to allow only one frontend server like for these case,(https://ui.cryptids.com), 
# and any other http headers or methods communicate with yuor server we use CORSmiddlewear

app.add_middleware(
    CORSMiddleware,
    allow_origins =["https://ui.cryptids.com"],
    allow_credentials=True,
    allow_methods={"*"},
    allow_headers=["*"]
)

@app.get("/test_cors")
def test_cors(request:Request):
    print(request)

    
@app.get('/')
def top():
    return "top here"


@app.get("/echo/{thing}")
def ech(thing):
    return f"echoing {thing}"

if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)