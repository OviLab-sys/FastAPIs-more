from fastapi import FastAPI,Body, Header, Response
import datetime,pytest,json
from fastapi.encoders import jsonable_encoder

app = FastAPI()


@app.post("/hi/")
def greet(who: str=Header()):
    return f"Hello {who} !"


@app.get("/header/{name}/{value}")
def header(name:str,value:str, response:Response):
    response.headers[name]=value
    return 'normal body'

@pytest.fixture
def data():
    return datetime.datetime.now()

def test_json_dump(data):
    with pytest.raises(Exception):
        _ = json.dumps(data)

def test_encoder(data):
    out = jsonable_encoder(data)
    assert out
    json_out = json.dumps(out)
    assert json_out

if __name__=="__main__":
    import uvicorn

    uvicorn.run("hello:app", reload=True)