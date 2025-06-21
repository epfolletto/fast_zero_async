from fastapi import FastAPI

from fast_zero_assync.routers import auth, todos, users

app = FastAPI(title='título teste')

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(todos.router)


@app.get('/')
def read_root():
    return {'message': 'Olá mundo!'}
