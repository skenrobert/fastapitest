from fastapi import APIRouter, HTTPException, status
from typing import Union
from db.models.user import User #instantiating the User model that is in db
from db.schemas.user import user_schema, users_schema # schema to read db
from db.client import db_client # conetion db
from bson import ObjectId #obj at id for search 

router = APIRouter(prefix="/usersdb",# prefix this page
                   tags=["usersdb"],# for swagger documentation 
                   responses={status.HTTP_404_NOT_FOUND: {"message":"no found"}})# overrall error 404 

  

#http://127.0.0.1:8000/usersdb
# @router.get("/usersdb",  response_model=list[User], status_code=200)
@router.get("/",  response_model=list[User], status_code=status.HTTP_200_OK)
async def users():
    try:
        return users_schema(db_client.local.users.find())
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="users no found")
        
    
#path
#http://127.0.0.1:8000/usersdb/1
# @router.get("/usersdb/{id}", response_model=User, status_code=200)
@router.get("/{id}", response_model=User, status_code=status.HTTP_200_OK)
async def show_userpath(id: str):
    return search_user("_id", ObjectId(id))
    
#query
#http://127.0.0.1:8000/usersdb/?id=1
# @router.get("/usersdb/", response_model=User, status_code=200)
@router.get("/", response_model=User, status_code=status.HTTP_200_OK)
async def show_userquery(id: str):
    return search_user("_id", ObjectId(id))
   
   
#http://127.0.0.1:8000/usersdb
# {
#   "username": "kenny3",
#   "email": "middle name and lastname",
# }
# @router.post("/usersdb", response_model=User, status_code=201)
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def store(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user already exists")
   
    user_dist = dict(user) # convert the user received by post into a dictionary(json)
    del user_dist["id"] # delete the id field since when it is created it creates all
    
    #we use local on local connections 
    id = db_client.local.users.insert_one(user_dist).inserted_id

    # _id name to default at mongo key attrib
    # insert_one, insert_many, find_one are python functions
    new_user = user_schema(db_client.local.users.find_one({"_id": id}))
    
    return User(**new_user)
    



# http://127.0.0.1:8000/usersdb/
# {
#   "id": "63ddb1c6e91571712cea8e40",
#   "username": "robert",
#   "email": "kenyyyn@gmail.com"
# }
@router.put("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def update(user: User):
    
    user_dict = dict(user)
    del user_dict["id"]

    try:
        db_client.local.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)
    except:
        return {"error": "No se ha actualizado el usuario"}

    return search_user("_id", ObjectId(user.id))#checking what is in the database, redundancy
        
        
# @router.delete("/users/{id}", response_model=User, status_code=200)
@router.delete("/{id}", response_model=User, status_code=status.HTTP_200_OK)
async def delete(id: str):
    
    found = db_client.local.users.find_one_and_delete({"_id": ObjectId(id)})
    print(found)   
     
    if not found:
        raise HTTPException(status_code=409, detail="user was not deleted")
    #else: #the raise that is above breaks the function you can omit the else and put it pasted return user the same if it does not enter it sends it
    return found

    
#**********************************************************************
 # function no exposed or do not consume directly   

def search_user(field: str, key):

    try:
        user = db_client.local.users.find_one({field: key})
        return User(**user_schema(user))
    except:
        return {"error": "No se ha encontrado el usuario"}


