"""
    Main app, loads the FastAPI with uvicorn server
    and contains our data.
"""
from typing import Optional

from fastapi import (FastAPI, Header, HTTPException, Path, Query, Response,
                     status)
from model import Person

# from fastapi.responses import JSONResponse Bugging 

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
async def get_person(id: int = Path(default=None,title="Person ID"\
                    ,description='Could be between 1 - 3',gt=0,le=3)): \
                    # gt -> greater than | lt -> less than or equal \
                    # Will customize our error message
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

@app.delete('/people/{id}')
async def delete_person(id: int):
    """
        Deleting a item.
    """
    try:
        del people[id]
        # Bugging
        # return JSONResponse(
            # status_code=status.HTTP_204_NO_CONTENT
            # ,content=people
            # )
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except KeyError as exk:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
            ,detail=f'ID: {id} not found'
        ) from exk

@app.get('/calc')
async def get_calc(a: float,b: float = Query(default=None,le=10)\
                    ,c: Optional[float] = None \
                    ,x_creator: str = Header(default="Kaique")):
                    # Header, used to use some data that can come on the Header
                    # Query has the same function that the Path
    """
        Calculating by a query parameter
    """
    print (f"Creator: {x_creator}")
    return {"sum": a+b+c if c else a+b}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app",host="127.0.0.1",port=8000,log_level="info"\
                ,reload=True)
