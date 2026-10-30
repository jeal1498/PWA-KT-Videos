# Videos de Karen Trujillo

Videos de marca personal (Instagram, TikTok, YouTube Shorts, Facebook). Una carpeta por video: `NN - Nombre/` con `video.mp4`, `portada.png`, `copy.md` y `guion.md`; `NN` es el orden de subida. Fechas y estado en `calendario.md`; copy listo para pegar en `tabla-publicacion.md`.

Se trabaja con dos skills de este repo: `.claude/skills/guiones-karen` (guiones) y `.claude/skills/videos-karen` (producción). Índice de la documentación en `docs/README.md`.

## Página de calendario

`index.html` es la agenda de videos (mes, video del día con su copy, reproductor y descarga). Lee `web/data.json`, que genera `python3 -I scripts/exportar_web.py` desde `calendario.md` y cada `copy.md`; `guardar.sh` lo corre solo. Tiene `noindex`. Para verla en línea: Settings → Pages → Deploy from a branch → `main` / root (`https://jeal1498.github.io/PWA-KT-Videos/`).
