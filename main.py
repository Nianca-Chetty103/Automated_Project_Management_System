from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, projects, github, messages

app = FastAPI(title="DevFlow")

app.add_middleware(CORSMiddleware, allow_origins=["*"],
    allow_methods=["*"], allow_headers=["*"])

app.include_router(auth.router,     prefix="/api/auth")
app.include_router(projects.router, prefix="/api/projects")
app.include_router(github.router,   prefix="/api/github")
app.include_router(messages.router, prefix="/api/messages")

# Serve the frontend
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
