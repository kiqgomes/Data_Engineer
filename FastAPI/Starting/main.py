# To deploy on terminal with uvicorn
#  uvicorn 'python_code':'FastAPI_name_declaration'
# Deploy with watcher to reload your modifications add '--reload'

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    """
        API base
    """
    return {"root": "Say Hello"}

@app.get('/msg')
async def message():
    """
        Hello message
    """
    return {"msg":"Hey bro!"}

# We can use the code below to deploy our API by a python startup on terminal
if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app",host="127.0.0.1",port=8000,log_level="info"\
                ,reload=True)
# Using python 'app_name'.py on terminal, it's same that what we did before, but now on the python code
