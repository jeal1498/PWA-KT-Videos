# Documentación

| Archivo | Qué es |
|---|---|
| `pendientes.md` | Lo que falta: siguiente número, días libres, avance de las v2 y temas abiertos |
| `plan-contenido-30-dias.md` | Plan de 30 días (12 oct 2026); puede traer precios y duraciones viejos: revisar con Karen |
| `historia/memory-hasta-2026-10-30.md` | `memory.md` completo antes de la reorganización: lecciones de V11 a V25, decisiones y estado de cada sesión |
| `historia/skill-videos-karen-hasta-2026-10-30.md` | `SKILL.md` anterior (flujo de una aprobación por etapa) |
| `historia/v2-sin-cara-README-hasta-2026-10-30.md` | README de las v2 sin cara (estilo, voz y trampas; lo vigente pasó a `references/estilo-v2.md`) |

## Reorganización del 30 oct 2026

`CLAUDE.md` y `memory.md` quedaron solo con lo vigente; la skill `videos-karen` se dividió en `guiones-karen` y `videos-karen`, el flujo pasó a lotes con dos aprobaciones y lo mecánico pasó a scripts (`nuevo.sh`, `armar.sh`, `portada.sh`, `copy.py`, `calendario.py`, `guardar.sh`, `qc.py`).

**Se borró, recuperable de git** (último commit antes de la reorganización: `6ba26bec9dcf27286e34c45f3e83230555fa9fb7`):

| Qué | Cómo se recupera |
|---|---|
| Ejemplos v2 del 19 al 24 (`build.py`, `scenes.py`, `anim.js`, `avs.json`, `words.json`, `warp.json`, portadas HTML, `prueba-6s.html`, `words-fernando.json`) | `git checkout 6ba26be -- .claude/skills/videos-karen/v2-sin-cara/` |
| Specs con cara 1 a 16 (`ejemplos/videoN-spec.json`; quedan el 17 y el de escenas) | `git checkout 6ba26be -- .claude/skills/videos-karen/ejemplos/` |
| `renderizar.sh` y `revisar.sh` (los sustituyen `armar.sh` y `qc.py`) | `git checkout 6ba26be -- .claude/skills/videos-karen/scripts/renderizar.sh .claude/skills/videos-karen/scripts/revisar.sh` |

El ejemplo del 25 quedó como `videos-karen/plantilla-v2/`. `voz.py` y `avatares.cjs` se movieron a `videos-karen/scripts/`, y `avatar-karen.cjs` (sin usar) a `videos-karen/assets/`.
