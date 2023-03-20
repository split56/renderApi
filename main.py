import os
from fastapi import FastAPI
import random
from fastapi.responses import FileResponse

app = FastAPI()

@app.get('/')
async def root() :
    return {'testing':'testing'}

@app.get('/random')
def read_item():
    path = "D:/minh/peiyanggit/photos"
    files = os.listdir(path)
    randomfile = random.choice(files)
    image = path + '/' + randomfile
    return FileResponse(image)