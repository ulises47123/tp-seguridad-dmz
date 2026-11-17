# TP 7 – Seguridad en Redes: diseño de una DMZ

Trabajo práctico de **Seguridad Informática** (Tecnicatura Superior en Soporte de Infraestructura de TI, 3.er año). Caso de aplicación: diseñar la DMZ de una institución educativa que necesita publicar su sitio web sin exponer la red interna (segmentos de estudiantes, docentes y administración).

## Archivos

- `TP7_DMZ_Ulises_Cabezas.html`: informe completo (riesgos, esquema de red con firewall y DMZ, qué servicios van en la DMZ y cuáles en la red interna, reglas de firewall y recomendaciones).
- `TP7_DMZ_Ulises_Cabezas.pdf`: el mismo informe en PDF.
- `convertir_pdf.py`: genera el PDF a partir del HTML con Playwright (Chromium).

## Regenerar el PDF

```bash
pip install playwright
playwright install chromium
python convertir_pdf.py
```
