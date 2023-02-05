from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

#not in the main for example basic auth
app = FastAPI()


router = APIRouter(prefix="/basicauth",
                   tags=["basicauth"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "Not found"}})


oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disable: bool

    
    
class UserDB(User):
    password: str
    
users_db = {
    "robert" : {
        "username": "robert",
        "full_name": "robert parra",
        "email": "test@test.com",
        "disable": True,
        "password": "123456"
    },
    "skenrobert" : {
            "username": "skenrobert",
            "full_name":"kenny mora",
            "email": "test@test.com",
            "disable": False,
            "password": "654321"
    }
}


#***************************Funtions************************************
def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username]) #(**)that can go several parameterss
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="hinbality authorization credentials",
            headers={"WWW-Autenticate": "Bearer"})
    
    if user.disable:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="inactive user")
        
        
    return user
            
            
        

#***************************************************************
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="user is not correct")
 
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="password is not correct")
 
    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user