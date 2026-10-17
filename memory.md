# Memory — Preferencias y Aprendizajes

## Tono y comunicación

- Directo y eficiente, sin introducciones. Respuestas concisas, sin textos largos.
- Actualizar este archivo de forma proactiva cuando el usuario indique nuevas preferencias; confirmar en el chat.

## Videos de Karen

- Flujo con una aprobación por etapa (ver la skill). Orden desde el 17 oct 2026: transcripción → tabla → portada → video → copy → hecho. Cada etapa se envía y se espera su «aprobado».
- La portada va como primer cuadro del video y debe quedar entre y=300 y y=1620 (Instagram la recorta a 3:4).
- Encuadre de ojos fijo en la línea del tercio superior (`encuadre.py`), sin seguimiento de movimiento.
- Los cambios aprobados se suben directo a `main`.
- Numeración: 01 a 05 y 07 confirmadas; el 06 queda reservado para otro video.

## Repo

- Este repo se creó el 17 oct 2026 para sacar los videos del repo del portafolio (pesaban ~290 MB y ese repo es público). La skill `videos-karen` se movió aquí.
- Pendiente: borrar `marketing/videos/` y `videos/` del historial del repo del portafolio. Requiere `git filter-repo --path marketing/videos --path videos --invert-paths` y force-push a `main` (el SHA anterior de `main` es `fa5d09f`). El clasificador de permisos de la sesión lo bloqueó; Eduardo puede darlo de alta como regla de Bash o hacerlo desde Termux.
