from fastapi import FastAPI
from routers import products, users, jwt_auth, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# print('hello')

#***************************routers****************

app.include_router(jwt_auth.router) #login yes bearer token jwt
app.include_router(products.router) # not bearer token
app.include_router(users.router)# not bearer token
app.include_router(users_db.router)# not bearer token

#http://127.0.0.1:8000/static/images/default.jpg
app.mount("/static", StaticFiles(directory="static"), name="static")
#behind if I show view resourses static            
# *************************************************

@app.get('/')
async def home():
    return {"Hello FastAPI"}

@app.get('/page1')
async def page1():
    radius = 10
    pi = 3.14
    area = pi
    result = 'The area of circle with {} is {}'.format(str(radius), str(area))
    return {result}


