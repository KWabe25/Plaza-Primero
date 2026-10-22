from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parent
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_page(viewport={"width":1280,"height":800});pg.goto((ROOT / "index.html").as_uri())
    for i,n in enumerate(["01_demanda","02_cursos","03_usuario","04_semaforo"]):
        pg.evaluate(f"go({i})");pg.screenshot(path=n+".png")
    pg.evaluate("go(2)")
    for s,n in [(1,"03b_usuario_registro"),(2,"03c_usuario_trabajo"),(4,"03d_usuario_certificado"),(5,"03e_usuario_ayuda_voz")]:
        pg.evaluate(f"st({s})");pg.screenshot(path=n+".png",full_page=True)
    b.close()
