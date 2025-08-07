from fastapi import FastAPI
from app import routes

app = FastAPI(
    title="Comment Microservice",
    description="Handles trails, users, and comments",
    version="1.0.0"
)

# Register routes
app.include_router(routes.router)

