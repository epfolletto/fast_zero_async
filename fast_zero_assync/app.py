from fastapi import FastAPI

from fast_zero_assync.routers import auth, users

app = FastAPI(title='título teste')

app.include_router(auth.router)
app.include_router(users.router)


@app.get('/')
def read_root():
    return {'message': 'Olá mundo!'}
