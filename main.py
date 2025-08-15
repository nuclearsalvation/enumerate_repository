from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse

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

@app.get('/query')
def get_model(name, num):
    return{'name':name,'num':num}

@app.get('/rdrct')
def redirect():
    return RedirectResponse('/text')