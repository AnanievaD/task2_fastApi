from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"Ананьева Дарья Сергеевна"}

@app.get('/tools')
async def f_indexT():
    return "Начальные навыки, не умею!"

@app.get('/users')
async def f_indexU():
    return "+79345345544"