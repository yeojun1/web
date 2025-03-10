from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory='templates')
app = FastAPI(docs_url=None, redoc_url=None)
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/favicon.ico')
async def _():
    return FileResponse('/static/favicon.ico')

@app.get('/')
async def _(request:Request):
    return templates.TemplateResponse('home.html',{'request':request})