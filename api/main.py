""" Main entry point of the app """

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.db import engine, Base
from api.routers import todolists, todoitems


# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="TodoList MCP API")

# CORS settings (optional, adjust origins as needed)
app.add_middleware(
    CORSMiddleware,          # Add CORS (Cross-Origin Resource Sharing) middleware to the FastAPI app
    allow_origins=["*"],     # Allow requests from *any* origin (any domain can access the API)
    allow_credentials=True,  # Allow cookies, authorization headers, or TLS client certificates to be included in requests
    allow_methods=["*"],     # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.) in cross-origin requests
    allow_headers=["*"],     # Allow all HTTP headers in cross-origin requests
)

# Include routers for API endpoints
app.include_router(todolists.router, prefix="/todolists", tags=["Todo Lists"])
app.include_router(todoitems.router, prefix="/todoitems", tags=["Todo Items"])

# Root endpoint
@app.get("/")
async def root(): return {"message": "TodoList MCP API running"}

