from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from schemas import UserSchema, UserPublic
from http import HTTPStatus

app = FastAPI()

# ...

@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
 return user
 ...