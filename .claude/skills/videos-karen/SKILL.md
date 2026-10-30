---
name: videos-karen
description: "Producir y guardar los videos de Karen Trujillo (neuropsicóloga, 9:16): voz clonada en ElevenLabs, animación a dos tintas con HyperFrames, edición de los videos que ella graba, portada, copy, control de calidad y subida al repo con calendario y página. Úsala siempre que haya guiones aprobados que producir, un video nuevo de Karen en Drive, o pidan render, portada, copy, calendario, «termina el lote», «guarda los videos» o corregir un video ya hecho, aunque no digan «skill». Para escribir guiones usa guiones-karen. No usar videos-checa."
---

# Producir videos de Karen

Tú (Claude) produces; Karen aprueba. El flujo es **por lote** con dos aprobaciones: (1) los guiones del lote (skill `guiones-karen`) y (2) el lote terminado. Entre una y otra no se le pide nada a nadie: si algo falla, se corrige y se sigue. Así se ahorra a Karen y a Eduardo revisar cada etapa de cada video (antes eran 5 aprobaciones por video).

`SK=.claude/skills/videos-karen`. Trabajo en el scratchpad (`<trabajo>` = una carpeta por video); al repo solo entra lo aprobado.

## Antes de empezar
- `git pull` y leer `docs/pendientes.md` (qué falta, fechas, avance de las v2).
- Videos grabados por Karen: carpeta de Drive `1VUra8EiQS0sDd22CKZCnpvy4Q5XMyYKV`. Listarla con `search_files` (`parentId`, `pageSize` alto) y comparar con el repo. Descargar con `curl -L "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t"` (el conector solo baja 10 MB). **Nunca usar `list_recent_files`:** devuelve documentos clínicos de pacientes.

## Producción de un lote (después de la aprobación 1)
Para cada video del lote, sin pedir aprobaciones intermedias:

1. `bash $SK/scripts/nuevo.sh <trabajo> guion.txt`: copia `plantilla-v2/` (la del 25) y deja `public/` listo.
2. **Voz:** `python3 -I $SK/scripts/voz.py <trabajo>/guion.txt <trabajo> --modelo v3 --max-silencio 0.35` → `voz.mp3` y `words.json`.
3. **Caras:** `NODE_PATH=<dir>/node_modules node $SK/scripts/avatares.cjs <trabajo>/avs.json clave:cara …` (una clave por aparición).
4. **Escenas:** reescribir `scenes.py` (HTML/SVG de cada escena con `sc(id, ini, fin, html)`) y los tiempos de `anim.js` (`B = [...]` y las entradas), anclados a `words.json`. Estilo, caras y trampas en `references/estilo-v2.md`: leerlo antes de la primera escena del lote.
5. **Vistazo:** `bash $SK/scripts/armar.sh <trabajo> --vistazo` → `vistazo-*.jpg` (un cuadro cada 2 s). Mirar las hojas: cuadros vacíos, textos encima del avatar, objetos irreconocibles. Corregir y repetir.
6. **Portada:** escribir `<trabajo>/portada.html` (partir del de la plantilla) con el gancho aprobado → `bash $SK/scripts/portada.sh <trabajo>`.
7. **Render:** `bash $SK/scripts/armar.sh <trabajo>` **con `run_in_background`** (6 a 9 min). Al terminar quedan `final.mp4` (voz, cola de 0.6 s para el aviso y portada como primer cuadro) y `prueba-720.mp4`. Se pueden lanzar los renders de varios videos uno tras otro mientras se escriben las escenas del siguiente.
8. **Copy:** `python3 -I $SK/scripts/copy.py <trabajo> NN "Nombre" "gancho" --de 08 [--evitar "12, 23"]` y llenar los `{HUECOS}`: título de YouTube (≤100 caracteres), texto IG/FB (el guion en prosa, sin tags), TikTok corto con pregunta, hashtags del tema y lo «por confirmar». Sin rayas largas, sin «no es X, es Y», sin listas «sin A, sin B», sin «cura» ni promesas. También `guion.md` con el encabezado de siempre (`# Guion NN (v2 del MM, sin cara)` + de dónde viene + el guion con tags).
9. **QC:** `python3 -I $SK/scripts/qc.py <trabajo>`. Todo ✗ se corrige antes de enseñar nada; los ! se miran.

## Aprobación 2: revisión del lote
Mandar con `SendUserFile` en un solo mensaje: los `prueba-720.mp4`, las portadas y los `copy.md`, más una tabla corta `NN · título · fecha propuesta · duración · lo que hay que confirmar`. Karen (o Eduardo por ella) responde «aprobado» o cambios por video. Solo se rehacen los videos con cambios, pasan `qc.py` otra vez y se reenvían solo esos.

## Guardar (con el lote aprobado)
- Fechas: `python3 -I $SK/scripts/calendario.py fechas 10` propone días libres con la alternancia (un día **sin cara**, otro **con Karen**). Las v2 van en días «sin cara». No poner seguidos videos del mismo tema.
- `bash $SK/scripts/guardar.sh lote.tsv` (una línea por video: `trabajo⇥NN⇥Nombre⇥gancho⇥fecha`). Copia todo a `NN - Nombre/`, actualiza `calendario.md`, `tabla-publicacion.md` y `web/`, corre `qc.py --repo` y hace **un solo commit** y push. Si el QC falla, no hay commit.
- Actualizar `docs/pendientes.md` (avance de las v2, siguiente número) en el mismo push o justo después.
- «Hecho» no es «Publicado»: «Publicado» solo lo marcan Karen o Eduardo.

## Videos grabados por Karen
El mismo esquema de lote: su guion entra en la aprobación 1 y el video editado en la 2. Los pasos técnicos (`preparar.sh`, `encuadre.py`, spec, `componer.py`, `portada.py`) están en `references/con-cara.md`; después se sigue igual con `armar.sh`, `copy.py`, `qc.py` y `guardar.sh`.

## Reglas que no cambian
- Orienta, no diagnostica: nunca «cura» ni diagnosticar por video. Todo video cierra con «Este video orienta y no diagnostica.» y `psicologakarentrujillo.com.mx`.
- Marca: ciruela `#433860`, ciruela profundo `#2E2545`, lavanda `#C6BCE2`, rosa `#F9DEE3`, arena `#F5E7D6`; Outfit (titulares) y Maven Pro (texto), ya en `assets/fonts/`. La fuente única de la identidad es `docs/marca/` del repo `jeal1498/Portfolio-Karen-Trujillo`; si algo choca, manda esa carpeta.
- Zona segura en todas las redes: contenido entre y=300 y y=1620 (Instagram recorta a 3:4).
- GitHub rechaza archivos de más de 100 MB; `armar.sh` deja `final.mp4` por debajo de 60 MB.
- Una v2 lleva su propio número y su `guion.md` dice de qué video viene; no publicarla seguida de su original.

## Aprender sobre la marcha
Al cerrar cada lote, agregar en una línea lo nuevo: preferencias de Karen o Eduardo en `memory.md` y trucos técnicos en `references/estilo-v2.md` o `con-cara.md`. Sin fechas ni historia: lo viejo ya está en `docs/historia/`. Si algo se volvió mecánico, convertirlo en script o en una revisión de `qc.py`.
