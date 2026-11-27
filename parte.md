# PARTE · 27 nov 2026

## ✓ Decidido
- nov1 a nov4 de Drive son los videos 36 (Instrucciones de una en una), 37 (Camuflaje en mujeres adultas), 38 (Qué esperar de la evaluación de tu hijo) y 39 (Dormir tarde por tiempo para ti).
- Video 36 aprobado con el estilo nuevo para videos con cara: subtítulos palabra por palabra con rebote, gráficos arriba y Karen abajo, animación por bloques (máx. 4 palabras, analogías literales), sin silencios y con color grading natural. Quedó en el skill `videos-karen` (`references/con-cara.md`).
- Color grading correctivo y sutil (blancos neutros, piel natural, fondo un poco menos saturado); sin viñeta, afilado ni saturación general.
- Skill `videos-karen` actualizada con lo aprendido: `recortar.py` (silencios), `color.sh` + `assets/karen.cube` (grading), `grade.py`, `scopes.py` y el ejemplo `ejemplos/video36-bloques.py`. Probada con el 37. Ya está en `main` (12 nov).
- 36 (jue 12 nov) y 37 (sáb 14 nov) guardados en el repo y en el calendario; Karen los sube en esas fechas. «Publicado» lo marcan ellos. El 37 se rehízo con el estilo nuevo y Karen lo aprobó.
- Copy único para Instagram, Facebook, TikTok y descripción de YouTube (mismo texto largo); solo cambia el título de YouTube (≤60 caracteres). Cada `copy.md` lleva SEO, GEO y AEO.
- 38 (lun 16 nov) y 39 (mié 18 nov) hechos con el estilo del 36, aprobados por Karen y guardados en `main` con calendario, tabla y página. Los videos 36 a 39 están hechos; solo falta el 40.
- Karen confirmó los «Por confirmar» de los copys 36, 37, 38 y 39 (el 39, el 13 nov).
- Con cara, el rótulo con cédula se sube a y≈620 (`.nametag{top:620px!important}` en el bloque custom) para no tapar los ojos.
- 41 Cobran la terapia si no voy (vie 4 dic): video 100 % gráfico y sin voz, aprobado el 15 nov y guardado en la rama de la sesión `ccr-5d2398ee-dcl86a` (falta pasarlo a `main`). Zona segura de TikTok (x 60 a 960, y 250 a 1440), centrado, loop (termina en la portada) y textos corregidos por Karen («terapia psicológica»). Recetas en `references/estilo-v2.md` y `loop.sh`.
- Hooks virales (voz en off de ElevenLabs, Karen sin cara): guiones de `hooks virales/` reescritos a tercera persona (001–028 y los de contenido nuevo 029–040); los diálogos de ejemplo entre comillas se dejaron igual.
- Hooks virales: se borraron las 9 carpetas viejas (solo encabezado) del 029 al 037; quedan 40 carpetas, una por número, con el guion completo.
- Voces de los hooks virales 001 a 030 aprobadas y guardadas en cada carpeta (`voz.mp3` + `words.json`): voz clonada de Karen en Eleven v3, CTA hablado al final, velocidad 1.10x (ffmpeg `atempo`, no gasta créditos). Plan ElevenLabs: Starter.
- ElevenLabs: la clave `ELEVENLABS_API_KEY` ya tiene permisos de lectura de voces y cuenta; plan Starter (39,781 créditos). La receta de los hooks virales es guion con CTA hablado, Eleven v3 y velocidad 1.10x (`atempo`); el guion 001 quedó recortado a 60 s.
- Hooks virales: gráficos del 001 aprobados (v4, 27 nov) y guardados en `graficos/`: pantalla completa sin Karen, 30 fps, sincronizados con la voz. La instrucción de Eduardo (acciones por bloque, ≤4 palabras, analogías literales, escala, persistencia, zonas seguras, escenas modulares) quedó en `references/hooks-virales.md` y `PLANTILLA-DISTRIBUCION.md` pasó a pantalla completa.
- Hooks virales: portada del 001 aprobada (estilo de los gráficos v4: «Es inteligente, pero no pone atención», bombilla y engranajes Comprender ≠ Atención); guardados `portada.png`, `graficos/portada.html` y `video.mp4` con la portada como primer cuadro y en bucle (el aviso final se funde 0.5 s en la portada; 60.8 s). Aprobado como receta para los siguientes: `final-hook.sh` (bucle + portada) y `plantilla-hooks/portada.html` en el skill.
- Hooks virales: 002 aprobado y guardado (gráficos, portada «¿Desobediente… o necesita otro apoyo?», `video.mp4` en bucle con portada como primer cuadro, 58 s).
- Hooks virales: 003 aprobado y guardado (portada «3 señales que se confunden con mala conducta», 69.6 s, bucle). Regla nueva de Eduardo: cada video con elementos gráficos nuevos (lista de usados en `references/hooks-virales.md`).
- Hooks virales: 004 aprobado y guardado con elementos nuevos (portada «¿3 horas jugando y 20 min de tarea no?», 65.6 s, bucle).
- Todo cambio a `parte.md` se guarda directo en `main` (Karen).

## … Falta
- Karen tiene que grabar el 40 (Cambios de rutina): no vino en Drive. Después: estilo del 36, fecha con `calendario.py` y `guardar.sh`.

- Karen confirma en el `copy.md` del 41: horas de aviso para cancelar, si deja «Netflix» y la cédula en el primer cuadro.
- Pasar el 41 de la rama de la sesión a `main`.

- Hooks virales 031 a 040: generar la voz con la receta cuando haya créditos (Starter no alcanzó para los 40; Eduardo los dejó pendientes).
- Hooks virales: faltan los gráficos del 005 al 040 (receta del 001 v4). Con 1.10x, 25 de las 30 voces pasan de 60 s (hasta 71 s en el 009): decidir si se recortan guiones.

## ✗ No tocar
- Diagnosticar o decir que algo «cura»: el contenido orienta, no diagnostica.
- `list_recent_files` de Drive: trae documentos de pacientes.
- Marcar «Publicado»: solo Karen o Eduardo.
