# Plaza Primero

Propuesta para **UINNOVA CONARE Reto 2**: empleo juvenil fuera de la GAM. Prototipo de una aplicación HTML con tres perspectivas:

- **Usuario** — primero el trabajo seguro, después el curso, y al final se confirma si la persona sigue empleada.
- **Instituciones** — panel del pacto territorial: demanda, brechas, semáforo público y pago por resultados.
- **Empresa** — registrar puestos, firmar el compromiso, ver candidatos y confirmar la contratación.

El prototipo está en la raíz (`index.html`, capturas PNG y `shot.py`). Nombres y cifras son de ejemplo.

## Cómo abrirla

Abra `index.html` en el navegador (doble clic o arrastre el archivo). No hace falta servidor ni instalación.

## Cómo regenerar las capturas

`shot.py` usa [Playwright](https://playwright.dev/python/) y Google Chrome en `/usr/bin/google-chrome`. Instale la dependencia y ejecute el script **desde la carpeta donde está**:

```bash
pip install playwright
python shot.py
```

El script abre el `index.html` de su misma carpeta (también `_resumen.html`) y guarda los PNG ahí.
