from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse

app = FastAPI()

@app.get('/')
def read_root():
    html_content = '<h2>enumerate</h2>'
    return HTMLResponse(content=html_content)

@app.get('/text', response_class=PlainTextResponse)
def root():
    data = 'enumerate'
    return PlainTextResponse(content=data)

@app.get('/text/{msg}')
def text_id(msg):
    return{"message":msg}