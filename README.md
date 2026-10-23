# Videos de Karen Trujillo

Videos de marca personal (Instagram, TikTok, YouTube Shorts, Facebook). Una carpeta por video: `NN - Nombre/` con `video.mp4`, `portada.png`, `copy.md` y `guion.md`. `NN` es el orden de subida. El estado de cada video está en `calendario.md`.

La edición se hace con la skill `videos-karen` del repo del portafolio (`jeal1498/Portfolio-Karen-Trujillo`).

`docs/plan-contenido-30-dias.md`: plan de contenido de 30 días (del 12 oct 2026, viene de la rama `claude/elegant-mccarthy-zoe14g` del portafolio). Puede traer precios y duraciones desactualizados: revisar con Karen antes de usarlo.

## Página de calendario (23 oct 2026)

`index.html` (raíz) es la agenda de videos: un mes que se desliza, el video del día con su copy (Instagram/Facebook, TikTok, YouTube), reproductor y descarga. Lee `web/data.json`, que genera `python3 -I scripts/exportar_web.py` a partir de `calendario.md` y de cada `copy.md`; hay que volver a correrlo y commitear `web/` cuando cambie el calendario o un copy. Tiene `noindex`. Para verla en línea: Settings → Pages → Deploy from a branch → `main` / root (`https://jeal1498.github.io/videos-karen-trujillo/`). Los videos se sirven desde sus carpetas (no se duplican). Las fechas marcadas «(propuesta)» en `calendario.md` las ajusta Karen.

