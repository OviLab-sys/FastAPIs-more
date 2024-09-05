from fastapi import FastAPI,Depends,params

app = FastAPI()

#the dependency function
def user_dep(name: str=params, password: str=params):
    return {"name":name, "valid":True}

@app.get("/user")
def get_user(user: dict=Depends(user_dep)) -> dict:
    return user

#if your dependency function just checks something and doesn't return anything,
#you can also define the dependency in your path decorator. as follows.
def check_dep(name: str = params, password: str=params):
    if not name: 
        raise

#the path fucnction/web endpoint
@app.get("/check_user", dependencies=[Depends(check_dep)])
def check_user()->bool:
    return True
