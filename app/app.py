from fastapi import FastAPI , HTTPException

app = FastAPI()

# CREATING A DUMMY ENDPOINT 
@app.get("/hello")
def hello():
    return "yo"

# creating text post
text_post = {1 : {"title" : "first post" , "content" : "hello new project"}}

@app.get('/posts')
def get_post( limit : int = None):
    if(limit):
        return list(text_post.values())[limit]
    return text_post

# returning a single post
@app.get('/posts/{id}')
def single_post(id : int):
    if(id not in text_post):
        raise HTTPException(status_code = 404 , detail = "post not available or found")
    
    return text_post.get(id)
