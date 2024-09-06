from fastapi import FastAPI
import uvicorn

app1=FastAPI()

@app1.get('/')
def home():
    return {"message": "Good bye"}

@app1.get('/welcome')
def welcome(name:str=None,age:int=None):
    return {"Name":name,"Age":age}




if __name__ == '__main__':
    uvicorn.run(app1,host='127.0.0.1',port=5000)