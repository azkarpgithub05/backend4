from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/spp", response_class=HTMLResponse)
async def form_spp(request: Request):
    return templates.TemplateResponse("spp_form.html", {"request": request})

@router.post("/spp", response_class=HTMLResponse)
async def handle_spp(request: Request, nama: str = Form(...), jumlah: int = Form(...)):
    return templates.TemplateResponse("spp_success.html", {"request": request, "nama": nama, "jumlah": jumlah})
