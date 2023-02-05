from pymongo import MongoClient

# db_client = MongoClient() # local at the code
# db_client = MongoClient().local # local here and not the code
db_client = MongoClient("mongodb+srv://toor:3dNoI3hGvPR46FEt@cluster0.8jxxjrk.mongodb.net/?retryWrites=true&w=majority").test # test name data base
# mongodb://localhost:27017 #default address (local mongoDB extension vcode)



#C:\Users\Kenny Robert\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\fastapitest