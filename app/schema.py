from pydantic import BaseModel # basemodel is a special object

class PostCreate(BaseModel): # inheriting basemodel 
    title : str              # used this to ricieve the data inside a func 
    content : str

class PostResponse(BaseModel):
    title : str
    content : str