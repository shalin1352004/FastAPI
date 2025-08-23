from fastapi import FastAPI
from routes.ItemRoute import router as ItemRouter
from routes.CategoryRoute import router as CategoryRouter
from routes.RoleRoute import router as RoleRouter
from routes.UserRoute import router as UserRouter
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Only allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ItemRouter)
app.include_router(CategoryRouter)
app.include_router(RoleRouter)
app.include_router(UserRouter)
@app.get("/")
async def root():
    return {"message": "Welcome to the Learning Tool API"}