# Videos de Karen Trujillo (Marca Personal)

Repo privado con los videos de marca personal de Karen Trujillo, neuropsicóloga clínica en Cancún (TDAH y autismo). El sitio web vive en otro repo: `jeal1498/Portfolio-Karen-Trujillo` (de ahí salen `DESIGN.md` y `PRODUCT.md`, la marca).

> **Preferencias del usuario:** leer `memory.md` al inicio de cada sesión. Actualizarlo proactivamente cuando el usuario indique nuevas preferencias.

## Cómo se trabaja

- Todo se hace con la skill `.claude/skills/videos-karen` (flujo con **una aprobación por etapa**: transcripción → tabla de elementos → portada → video → copy → hecho). Leer su «Estado y pendientes» al empezar.
- Fuente de los videos: carpeta de Drive de la skill. Antes de editar: `git pull origin main`.
- Cada video vive en `NN - Nombre/` (`NN` = orden de subida) con `video.mp4`, `portada.png`, `copy.md` y `guion.md`. El estado está en `calendario.md`. «Hecho» no es «Publicado».
- El `video.mp4` final se commitea **una sola vez, ya aprobado** (portada incluida como primer cuadro; GitHub rechaza archivos de más de 100 MB). Commit y push directo a `main`.
- Las versiones de prueba se mandan con `SendUserFile` desde el scratchpad y no se commitean.
- Es información de ayuda, no diagnóstico: nunca afirmar que algo «cura» ni diagnosticar por video.
