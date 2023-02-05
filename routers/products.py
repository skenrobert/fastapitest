from fastapi import APIRouter

router = APIRouter(prefix="/products",# prefix this page
                   tags=["products"],# for swagger documentation 
                   responses={404: {"message":"no found"}})# overrall error 404 

products_list = ["Product 1", "Product 2", "Product 3"]

#root of your fastapi framework then (when there are no routes)
#python3 -m uvicorn products:app --reload (run only this page)
@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id: int):
    return products_list[id]