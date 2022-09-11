"""
    Main app, loads the FastAPI with uvicorn server
    and contains our data.
"""
from fastapi import FastAPI, HTTPException, status, jsonResponse
from model import Person

people = {
    1: {
        "name": "Kaique Gomes"
        ,"age": 19
        ,"alive": True
    }
    ,
    2: {
        "name": "Jimmy McGill"
        ,"age": 52
        ,"alive": False
    }
    ,
    3: {
        "name": "Jesse"
        ,"age": 24
        ,"alive": None
    }
}

app = FastAPI()

@app.get('/')
async def get_root():
    """
        API base
    """
    return {"msg" : "Hey Brother"}

@app.get('/people')
async def get_people():
    """
        Get all database
    """
    return people

@app.get('/people/{id}')
async def get_person(id: int):
    """
        Get a specific person and handling with errors.
    """
    try:
        return people[id]
    except KeyError as exk:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
            ,detail= "Pearson Not Found"
        ) from exk

@app.post('/person',status_code=status.HTTP_201_CREATED)
async def post_person(person: Person):
    """
        Adding new people to database.
    """
    people[len(people) + 1] = person
    del person.id
    return person

@app.put('/people/{id}')
async def put_person(id: int,person: Person):
    """
        Update a existent item.
    """
    if id in people:
        people[id] = person
        person.id = id
        return person
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
            ,detail=f"ID: {id} don't exists"
        )

@app.delete('/people/{id}', status_code=)
async def delete_person(id: int):
    """
        Deleting a item.
    """
    try:
        del people[id]
        return people
    except KeyError as exk:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
            ,detail=f'ID: {id} not found'
        ) from exk

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app",host="127.0.0.1",port=8000,log_level="info"\
                ,reload=True)
