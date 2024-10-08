from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

# Montar carpeta de archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar Jinja2 para usar plantillas
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/projects")
async def read_projects(request: Request):
    # Simular una lista de proyectos
    projects = [
        {"title": "Project 1", "description": "Description of project 1"},
        {"title": "Project 2", "description": "Description of project 2"},
        {"title": "Project 3", "description": "Description of project 3"},
    ]
    return templates.TemplateResponse("projects.html", {"request": request, "projects": projects})
