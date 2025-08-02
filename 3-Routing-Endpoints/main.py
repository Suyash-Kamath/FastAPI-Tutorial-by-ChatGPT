from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {'data':'blog list'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/{id}/comments')
def comments(id:int):
    return {'data':{'1','2'},'id':id}   


@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}


if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)