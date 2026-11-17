# Convierte el informe HTML a PDF usando Playwright (Chromium)
from pathlib import Path
from playwright.sync_api import sync_playwright

carpeta = Path(__file__).parent
html = carpeta / "TP7_DMZ_Ulises_Cabezas.html"
pdf = carpeta / "TP7_DMZ_Ulises_Cabezas.pdf"

with sync_playwright() as p:
    navegador = p.chromium.launch()
    pagina = navegador.new_page()
    pagina.goto(html.resolve().as_uri(), wait_until="networkidle")
    pagina.evaluate("document.fonts.ready")
    pagina.pdf(path=str(pdf), format="Letter", print_background=True, prefer_css_page_size=True)
    navegador.close()

print("PDF generado:", pdf)
