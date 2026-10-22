from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parent
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_page(viewport={"width":1440,"height":1000});pg.goto((ROOT / "index.html").as_uri())
    U=["bienvenida","registro","trabajos","curso","progreso","certificado","seguimiento","ayuda_voz"]
    for i,n in enumerate(U):
        pg.evaluate(f"U({i})");pg.wait_for_timeout(350);pg.locator("#phone").screenshot(path=f"usuario_{i+1:02d}_{n}.png")
    pg.evaluate("U(0)");pg.wait_for_timeout(350);pg.screenshot(path="usuario_00_vista_completa.png")
    pg.evaluate("P(1)");pg.wait_for_timeout(400)
    pg.screenshot(path="instituciones_00_completo.png",full_page=True)
    for s,n in [("#d1","mercado"),("#d2","brechas"),("#d3","semaforo"),("#d4","pago_resultados")]:
        pg.locator(s).screenshot(path=f"instituciones_{n}.png")
    pg.evaluate("P(2)")
    for i,n in enumerate(["registrar_puestos","firmar_compromiso","candidatos","confirmar_contratacion"]):
        pg.evaluate(f"E({i})");pg.wait_for_timeout(350);pg.set_viewport_size({"width":1440,"height":560});pg.screenshot(path=f"empresa_{i+1:02d}_{n}.png",full_page=True)
    b.close()
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_page(viewport={"width":1920,"height":1080});pg.goto((ROOT / "_resumen.html").as_uri());pg.wait_for_timeout(500)
    pg.screenshot(path="00_resumen.png");b.close()
