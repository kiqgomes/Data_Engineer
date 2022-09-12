from fastapi import FastAPI
from pydantic import BaseModel


class Person(BaseModel):
    id: int
    name: str
    age: int
    online: bool = True 

app = FastAPI()

people = [
    Person(id=1,name="Claudio",age=25)
    , Person(id=2,name="Pedro",age=32)
    , Person(id=3,name="Cleitu",age=85)
    , Person(id=4,name="Astolfo",age=12)
    , Person(id=5,name="Kaique",age=19)
]

@app.get('/')
async def index():
    return {"Possible":["/age/name","/info/name"]}

@app.get('/age/{name}')
async def age(name: str):
    for Person in people:
        if Person.name == name:
            return {"Age": Person.age}
    return None

@app.get('/info/{name}')
async def info(name: str):
    for Person in people:
        if Person.name == name:
            return Person
    return None

@app.put('/Person/{id}/{new_status}')
async def online(id: int,new_status: str):
    for Person in people:
        if Person.id == id:
            Person.online = False if new_status == "off" else True
            return Person
    return None

"""
To up 
> uvicorn FILE_NAME:APP_NAME --reload
"""