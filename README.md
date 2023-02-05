#fastapitest
 basic login and login jwt with fastapi 

#the first thing to do is install fastapi the only prerequisite is python 
pip install fastapi
pip install fastapi[all]
pip install "uvicorn[standard]"

#at windows could add edit the system environment variables (in case of developing in windows)

#execute server:
python -m uvicorn main:app --reload
python3 -m uvicorn main:app --reload
#stop server with CTRL + C

#it already has the routes established, therefore when executing the server in the main the routes already work 

#swagger documentation of the api in real time (local)
http://127.0.0.1:8000/docs
#cloud in deta free server
https://j8h2ff.deta.dev/docs#/

#there is other documentation local or at cloud 
http://127.0.0.1:8000/redoc
#cloud
https://j8h2ff.deta.dev/redoc

#debugger jwt
https://jwt.io/
https://token.dev/

#bycrypt-generator
https://bcrypt-generator.com/

#mongodb
#this framework to work api used with mongodb is very fast but it does not natively allow relationships, although it can be forced it is not recommended

#This project is running on free servers both the database and the API
db/client.py 
#points to a free database in mongodb

#deta is a free server for fastapi and node.js
https://j8h2ff.deta.dev/

