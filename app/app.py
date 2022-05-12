from app.schemas import API_output
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Body, FastAPI, Query
from typing import Dict, List
from .examples import examples
import yaml


from .library.helpers import *
from app.routers import twoforms, unsplash, accordion


app = FastAPI()


templates = Jinja2Templates(directory="templates")


with open("app/config.yaml") as file:
    configs = yaml.load(file, Loader=yaml.FullLoader)

app = FastAPI(
    title="toxicity detection",
    version=configs["versions"]["api"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(unsplash.router)
app.include_router(twoforms.router)
app.include_router(accordion.router)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = openfile("home.md")
    return templates.TemplateResponse("page.html", {"request": request, "data": data})

@app.get("/portfolio_details", response_class=HTMLResponse)
async def portfolio_details(request: Request):
    # data = openfile("portfolio.md")
    return templates.TemplateResponse("portfolio-details.html",  {"request": request})



@app.get("/predict", response_model=API_output)
async def read_items(q: str = Query(..., min_length=3), example=examples) -> Dict[List[Dict[str, float]], List[str]]:
    if q:
        score = len(q)
        return {
            "data": {
                "sentence": q,
                "score": score,
            },
            "versions": configs["versions"],
        }
