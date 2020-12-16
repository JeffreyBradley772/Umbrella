import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get('/')
def index():
    return{
    "message": "Hello World",
    "Status" : "OK"
    }

uvicorn.run(api)
