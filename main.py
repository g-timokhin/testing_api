import random

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def items():
    return [{"name":"item1"},{"name":"item2"}]

#Определим модель для тела post-запроса
class Payload(BaseModel):
    name: str

#Определим функции, возвращающие число кратное 3 строго в одном случае из трех
x = [1,2,3]

def random_pop(x):
  resp = x.pop(random.randrange(len(x)))
  return resp

def get_1_of_3():
  global x
  if x:
    return random_pop(x)
  else:
     x = [1,2,3]
     return random_pop(x)

@app.post("/")
async def add(payload: Payload):
  n = get_1_of_3()
  if n % 3 == 0:
    raise HTTPException(status_code=404, detail={"status":"error"})
  else:
    return {'status':'ok'}