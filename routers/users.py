from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Union

router = APIRouter(prefix="/users",# prefix this page
                   tags=["users"],# for swagger documentation 
                   responses={404: {"message":"no found"}})# overrall error 404 


class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    is_active: Union[bool, None] = None
    
users_list = [User(id=1,name="robert", surname="middle name and lastname", age=35),
              User(id=2,name="kenny", surname="middle name and lastname", age=35)]

##http://127.0.0.1:8000/basicjson
@router.get("/basicjson")
async def users():
    return [{"name":"robert", "surname":"middle name and lastname", "age":35},
            {"name":"kenny", "surname":"middle name and lastname", "age":35}]

#http://127.0.0.1:8000/users
# @router.get("/users",  response_model=list[User], status_code=200)
@router.get("/",  response_model=list[User], status_code=200)
async def users():
    try:
        return users_list
    except:
        raise HTTPException(status_code=404, detail="users no found")
        
    
#path
#http://127.0.0.1:8000/users/1
# @router.get("/users/{id}", response_model=User, status_code=200)
@router.get("/{id}", response_model=User, status_code=200)
async def show_userpath(id: int):
    return search_user(id)
    
#query
#http://127.0.0.1:8000/users/?id=1
# @router.get("/users/", response_model=User, status_code=200)
@router.get("/", response_model=User, status_code=200)
async def show_userquery(id: int):
    return search_user(id)
   
   
#http://127.0.0.1:8000/users
# {
#   "id": 3,
#   "name": "kenny3",
#   "surname": "middle name and lastname",
#   "age": 35,
#   "is_active": null
# }
# @router.post("/users", response_model=User, status_code=201)
@router.post("/", response_model=User, status_code=201)
async def store(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="user already exists")
    
    users_list.routerend(user)
    return user
    
#http://127.0.0.1:8000/users
# {
#   "id": 3,
#   "name": "KENNY ROBERT",
#   "surname": "middle name and lastname",
#   "age": 35,
#   "is_active": null
# }    
# @router.put("/users", response_model=User, status_code=201)
@router.put("/", response_model=User, status_code=201)
async def update(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            
    if not found:
        raise HTTPException(status_code=304, detail="user no update")
    #else: #the raise that is above breaks the function you can omit the else and put it pasted return user the same if it does not enter it sends it
    return user
        
        
# @router.delete("/users/{id}", response_model=User, status_code=200)
@router.delete("/{id}", response_model=User, status_code=200)
async def delete(id: int):
    found = False
    for index, delete_user in enumerate(users_list):
        if delete_user.id == id:
            user = delete_user
            del users_list[index]
            found = True
            
    if not found:
        raise HTTPException(status_code=409, detail="user was not deleted")
    #else: #the raise that is above breaks the function you can omit the else and put it pasted return user the same if it does not enter it sends it
    return user

    
#**********************************************************************
 # function no exposed or do not consume directly    
def search_user(id: int):
    #search in users_list
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return "user no found"
        




