from fastapi import FastAPI , HTTPException
from app.schema import PostCreate , PostResponse

app = FastAPI()

# CREATING A DUMMY ENDPOINT 
@app.get("/hello")
def hello():
    return "yo"

# creating text post
text_post = {   1 : {"title" : "first post" , "content" : "hello new project"},
                2 : {"title" : "second post" , "content" : "hello new project"},
                3 : {"title" : "third post" , "content" : "hello new project"},
                4 : {"title" : "fourth post" , "content" : "hello new project"},
                5 : {"title" : "fifth post" , "content" : "hello new project"},
                6 : {"title" : "sixth post" , "content" : "hello new project"},
                7 : {"title" : "seven post" , "content" : "hello new project"},
                8 : {"title" : "eight post" , "content" : "hello new project"},
                9 : {"title" : "nine post" , "content" : "hello new project"}
            }

@app.get('/posts')
def get_post( limit : int ):
    if(limit):
        return list(text_post.values())[:limit]
    return text_post

# returning a single post
@app.get('/posts/{id}')
def single_post(id : int):
    if(id not in text_post):
        raise HTTPException(status_code = 404 , detail = "post not available or found")
    
    return text_post.get(id)

# posting a data
@app.post('/posts')
def create_post(post : PostCreate) ->  PostResponse:
    text_post[max(text_post.keys()) + 1 ] = {"title" : post.title , "content" : post.content}
    new_post = {"title" : post.title , "content" : post.content}
    return new_post

# deleting data 
@app.delete('/posts')
def del_post():
    return